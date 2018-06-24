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
        self.assertTrue('API Submodules' in response)
        for element in ['databases', 'resources', 'admin', 'users', 'websites']:
            self.assertTrue(element in response['API Submodules'])

    def test_api_databases(self):
        client = app.test_client()
        r = client.get('api/databases/')
        response = json.loads(r.data.decode())
        expected = {'Database Submodules': ['mysql']}
        self.assertEqual(response, expected)

    def test_api_database_mysql(self):
        client = app.test_client()
        r = client.get('api/databases/mysql/')
        response = json.loads(r.data.decode())
        expected = {"API Module": "sassy.cortex.views.databases.mysql"}
        self.assertEqual(response, expected)

    def test_api_resources(self):
        client = app.test_client()
        r = client.get('api/resources/')
        response = json.loads(r.data.decode())
        self.assertTrue('Resource Submodules' in response)
        for element in ['containers', 'virtualmachines', 'hosts', 'providers']:
            self.assertTrue(element in response['Resource Submodules'])

    def test_api_resources_containers(self):
        client = app.test_client()
        r = client.get('api/resources/containers/')
        response = json.loads(r.data.decode())
        expected = {"Containers": "sassy.cortex.views.resources.containers"}
        self.assertEqual(response, expected)

    def test_api_resources_virtualmachines(self):
        client = app.test_client()
        r = client.get('api/resources/virtualmachines/')
        response = json.loads(r.data.decode())
        expected = {"VirtualMachines": "sassy.cortex.views.resources.virtualmachines"}
        self.assertEqual(response, expected)

    def test_api_resources_hosts(self):
        client = app.test_client()
        r = client.get('api/resources/hosts/')
        response = json.loads(r.data.decode())
        expected = {"Hosts": "sassy.cortex.views.resources.hosts"}
        self.assertEqual(response, expected)

    def test_api_resources_providers(self):
        client = app.test_client()
        r = client.get('api/resources/providers/')
        response = json.loads(r.data.decode())
        expected = {"Providers": "sassy.cortex.views.resources.providers"}
        self.assertEqual(response, expected)

    def test_api_admin(self):
        client = app.test_client()
        r = client.get('api/admin/')
        response = json.loads(r.data.decode())
        self.assertTrue('Admin Submodules' in response)
        for element in ['users']:
            self.assertTrue(element in response['Admin Submodules'])

    def test_api_admin_users(self):
        client = app.test_client()
        r = client.get('api/admin/users/')
        response = json.loads(r.data.decode())
        expected = {"Users": "sassy.cortex.views.admin.users"}
        self.assertEqual(response, expected)

    def test_api_users(self):
        client = app.test_client()
        r = client.get('api/users/')
        response = json.loads(r.data.decode())
        self.assertTrue('Users Submodules' in response)
        for element in ['manage_users']:
            self.assertTrue(element in response['Users Submodules'])

    def test_api_users_manage_users(self):
        client = app.test_client()
        r = client.get('api/users/manage_users/')
        response = json.loads(r.data.decode())
        expected = {"Manage_Users": "sassy.cortex.views.users.manage_users"}
        self.assertEqual(response, expected)

    def test_api_websites(self):
        client = app.test_client()
        r = client.get('api/websites/')
        response = json.loads(r.data.decode())
        self.assertTrue('Websites Submodules' in response)
        for element in ['website']:
            self.assertTrue(element in response['Websites Submodules'])

    def test_api_websites_website(self):
        client = app.test_client()
        r = client.get('api/websites/website/')
        response = json.loads(r.data.decode())
        expected = {"Website": "sassy.cortex.views.websites.website"}
        self.assertEqual(response, expected)

