import unittest
import os
import tempfile
import json
from sassy.cortex.app import app


class TestRoutes(unittest.TestCase):

    db_fd = 0

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        app.config['ENVIRON'] = 'development'
        client = app.test_client()
        with app.app_context():
            app.init_db()
        yield client

    def tearDown(self):
        try:
            os.close(self.db_fd)
            os.unlink(app.config['DATABASE'])
        except OSError:
            pass

    def test_api_base(self):
        client = app.test_client()
        r = client.get('api/')
        response = json.loads(r.data.decode())
        expected = {'API Submodules': ['databases', 'resources', 'admin', 'users', 'websites']}
        self.assertEqual(response, expected)

    def test_api_databases(self):
        client = app.test_client()
        r = client.get('api/databases/')
        response = json.loads(r.data.decode())
        expected = {'Database Submodules': ['mysql']}
        self.assertEqual(response, expected)
