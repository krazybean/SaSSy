import unittest
import os
import tempfile
from sassy.cortex.app import app


class TestBase(unittest.TestCase):

    db_fd = 0

    def setUp(self):
        db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        app.config['ENVIRON'] = 'development'
        client = app.test_client()
        with app.app_context():
            app.init_db()
        yield client

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_initial_route(self):
        client = app.test_client()
        r = client.get('/')
        print(r.data)
