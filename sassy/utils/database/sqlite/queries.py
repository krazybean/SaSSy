
class SqliteQueries(object):

    def __init__(self):
        pass


    def create_table_cms(self):
        return """CREATE TABLE "cms" (
          "id" INTEGER CONSTRAINT "pk_cms" PRIMARY KEY AUTOINCREMENT,
          "name" TEXT NOT NULL,
          "distro_url" TEXT NOT NULL,
          "description" TEXT NOT NULL
        );"""


    def create_table_database_users(self):
        return """CREATE TABLE "database_users" (
          "id" INTEGER CONSTRAINT "pk_database_users" PRIMARY KEY AUTOINCREMENT,
          "database_id" INTEGER,
          "database_username" TEXT NOT NULL,
          "connections" TEXT NOT NULL
        );"""

    def create_table_databases(self):
        return """CREATE TABLE "databases" (
          "id" INTEGER CONSTRAINT "pk_databases" PRIMARY KEY AUTOINCREMENT,
          "database_name" TEXT NOT NULL,
          "user_id" TEXT NOT NULL,
          "host_id" INTEGER
        );"""

    def create_table_device_attributes(self):
        return """CREATE TABLE "device_attributes" (
          "id" INTEGER CONSTRAINT "pk_device_attributes" PRIMARY KEY AUTOINCREMENT,
          "virtualmemory" TEXT,
          "cpu" TEXT,
          "virtualdisk" TEXT NOT NULL,
          "host_id" INTEGER
        );"""

    def create_table_devicetype(self):
        return """CREATE TABLE "devicetype" (
          "id" INTEGER CONSTRAINT "pk_devicetype" PRIMARY KEY AUTOINCREMENT,
          "name" TEXT NOT NULL,
          "description" TEXT
        );"""

    def create_table_hosts(self):
        return """CREATE TABLE "hosts" (
          "id" INTEGER CONSTRAINT "pk_hosts" PRIMARY KEY AUTOINCREMENT,
          "hostname" TEXT NOT NULL,
          "ip" TEXT,
          "provider_id" INTEGER,
          "device_type_id" INTEGER
        );"""

    def create_table_providers(self):
        return """CREATE TABLE "providers" (
          "id" INTEGER CONSTRAINT "pk_providers" PRIMARY KEY AUTOINCREMENT,
          "provider_name" TEXT NOT NULL,
          "provider_user" TEXT NOT NULL,
          "provider_key" TEXT NOT NULL,
          "provider_secret" TEXT NOT NULL
        );"""

    def create_table_roles(self):
        return """CREATE TABLE "roles" (
          "id" INTEGER CONSTRAINT "pk_roles" PRIMARY KEY AUTOINCREMENT,
          "name" TEXT NOT NULL,
          "permset" TEXT NOT NULL
        );"""

    def create_table_ssl(self):
        return """CREATE TABLE "ssl" (
          "id" INTEGER CONSTRAINT "pk_ssl" PRIMARY KEY AUTOINCREMENT,
          "certificate" TEXT NOT NULL,
          "private_key" TEXT NOT NULL,
          "intermediate" TEXT NOT NULL,
          "common_name" TEXT,
          "organizational_unit" TEXT,
          "organization" TEXT,
          "locality" TEXT,
          "state" TEXT,
          "country" TEXT
        );"""

    def create_table_users(self):
        return """CREATE TABLE "users" (
          "id" INTEGER CONSTRAINT "pk_users" PRIMARY KEY AUTOINCREMENT,
          "username" TEXT NOT NULL,
          "email_address" TEXT NOT NULL,
          "role_id" INTEGER
        );"""

    def create_table_websites(self):
        return """CREATE TABLE "websites" (
          "id" INTEGER CONSTRAINT "pk_websites" PRIMARY KEY AUTOINCREMENT,
          "domain_name" TEXT NOT NULL,
          "user_id" TEXT NOT NULL,
          "vhost_entry" TEXT,
          "ssl_id" INTEGER,
          "host_id" INTEGER,
          "cms_id" INTEGER,
          "path" TEXT
        )"""