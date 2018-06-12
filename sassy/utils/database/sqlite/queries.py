"""
Database Table creation
PreSeed data after initial creation
Base queries for SQLite
"""


class SqliteQueries(object):
    """ Base query class for cleaner queries"""

    def __init__(self):
        pass

    # Database table creation
    @staticmethod
    def create_table_cms():
        return """CREATE TABLE "cms" (
          "id" INTEGER CONSTRAINT "pk_cms" PRIMARY KEY AUTOINCREMENT,
          "name" TEXT NOT NULL,
          "distro_url" TEXT NOT NULL,
          "description" TEXT NOT NULL
        );"""

    @staticmethod
    def create_table_database_users():
        return """CREATE TABLE "database_users" (
          "id" INTEGER CONSTRAINT "pk_database_users" PRIMARY KEY AUTOINCREMENT,
          "database_id" INTEGER,
          "database_username" TEXT NOT NULL,
          "connections" TEXT NOT NULL
        );"""

    @staticmethod
    def create_table_databases():
        return """CREATE TABLE "databases" (
          "id" INTEGER CONSTRAINT "pk_databases" PRIMARY KEY AUTOINCREMENT,
          "database_name" TEXT NOT NULL,
          "user_id" TEXT NOT NULL,
          "host_id" INTEGER
        );"""

    @staticmethod
    def create_table_device_attributes():
        return """CREATE TABLE "device_attributes" (
          "id" INTEGER CONSTRAINT "pk_device_attributes" PRIMARY KEY AUTOINCREMENT,
          "virtualmemory" TEXT,
          "cpu" TEXT,
          "virtualdisk" TEXT NOT NULL,
          "host_id" INTEGER
        );"""

    @staticmethod
    def create_table_devicetype():
        return """CREATE TABLE "devicetype" (
          "id" INTEGER CONSTRAINT "pk_devicetype" PRIMARY KEY AUTOINCREMENT,
          "name" TEXT NOT NULL,
          "description" TEXT
        );"""

    @staticmethod
    def create_table_hosts():
        return """CREATE TABLE "hosts" (
          "id" INTEGER CONSTRAINT "pk_hosts" PRIMARY KEY AUTOINCREMENT,
          "hostname" TEXT NOT NULL,
          "ip" TEXT,
          "provider_id" INTEGER,
          "device_type_id" INTEGER
        );"""

    @staticmethod
    def create_table_providers():
        return """CREATE TABLE "providers" (
          "id" INTEGER CONSTRAINT "pk_providers" PRIMARY KEY AUTOINCREMENT,
          "provider_name" TEXT NOT NULL,
          "provider_user" TEXT NOT NULL,
          "provider_key" TEXT NOT NULL,
          "provider_secret" TEXT NOT NULL
        );"""

    @staticmethod
    def create_table_roles():
        return """CREATE TABLE "roles" (
          "id" INTEGER CONSTRAINT "pk_roles" PRIMARY KEY AUTOINCREMENT,
          "name" TEXT NOT NULL,
          "permset" TEXT NOT NULL
        );"""

    @staticmethod
    def create_table_ssl():
        return """CREATE TABLE "ssl" (
          "id" INTEGER CONSTRAINT "pk_ssl" PRIMARY KEY AUTOINCREMENT,
          "certificate" TEXT,
          "private_key" TEXT,
          "intermediate" TEXT,
          "common_name" TEXT,
          "organizational_unit" TEXT,
          "organization" TEXT,
          "locality" TEXT,
          "state" TEXT,
          "country" TEXT
        );"""

    @staticmethod
    def create_table_users():
        return """CREATE TABLE "users" (
          "id" INTEGER CONSTRAINT "pk_users" PRIMARY KEY AUTOINCREMENT,
          "username" TEXT NOT NULL,
          "email_address" TEXT NOT NULL,
          "role_id" INTEGER
        );"""

    @staticmethod
    def create_table_websites():
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

    # Validity checks
    @staticmethod
    def check_if_exists():
        return """SELECT name FROM roles;"""

    # Role Queries
    @staticmethod
    def role_get_all():
        return """SELECT id, name, permset FROM roles;"""

    @staticmethod
    def role_get_by_id():
        return """SELECT id, name, permset FROM roles WHERE name = ?"""

    @staticmethod
    def role_get_by_id():
        return """SELECT id, name, permset FROM roles WHERE id = ?"""

    @staticmethod
    def role_insert():
        return """ INSERT INTO roles (name, permset) VALUES (?, ?); """

    @staticmethod
    def role_update():
        return """UPDATE roles SET permset = ? WHERE name = ?; """

    @staticmethod
    def role_delete():
        return """DELETE FROM roles WHERE name = ?; """

    # Website Queries
    @staticmethod
    def website_get_by_id():
        return """ SELECT domain_name,
            user_id, vhost_entry, ssl_id,
            host_id, cms_id, path
            FROM websites WHERE id = ?;"""

    @staticmethod
    def website_get_by_name():
        return """ SELECT domain_name,
            user_id, vhost_entry, ssl_id,
            host_id, cms_id, path
            FROM websites WHERE domain_name = ?;"""

    @staticmethod
    def website_get_all_userid():
        return """ SELECT domain_name,
            user_id, vhost_entry, ssl_id,
            host_id, cms_id, path
            FROM websites WHERE user_id = ?;"""

    @staticmethod
    def website_insert():
        return """INSERT INTO websites (domain_name, user_id, path) VALUES (?, ?, ?);"""

    @staticmethod
    def website_update():
        return """UPDATE websites
            SET domain_name = ?,
                user_id = ?,
                vhost_entry = ?,
                ssl_id = ?,
                host_id = ?,
                cms_id = ?,
                path = ?
            WHERE domain_name = ?"""

    @staticmethod
    def website_delete():
        return """DELETE FROM websites where id = ?"""

    # SSL querires
    @staticmethod
    def ssl_get_by_id():
        return """ SELECT certificate,
            private_key, intermediate, common_name,
            organizational_unit, organization, locality,
            state, country FROM ssl WHERE id = ?;"""

    @staticmethod
    def ssl_insert():
        return """INSERT INTO ssl
            (certificate, private_key, intermediate,
             common_name, organizational_unit, organization,
             locality, state, country) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
   
    @staticmethod
    def ssl_delete():
        return """DELETE FROM ssl WHERE id = ?;"""

    # User queries
    @staticmethod
    def user_get_by_id():
        return """SELECT id, username, email_address, role_id FROM users WHERE id = ?;"""

    @staticmethod
    def user_get_by_username():
        return """SELECT id, username, email_address, role_id FROM users WHERE username = ?;"""

    @staticmethod
    def user_insert():
        return """INSERT INTO users (username, email_address, role_id) VALUES (?, ?, ?);"""

    @staticmethod
    def user_update():
        return """UPDATE users SET email_address = ?, role_id = ? WHERE id = ?;"""

    # Database Queries
    @staticmethod
    def database_get_by_user():
        return """SELECT id, database_name, user_id, host_id FROM databases WHERE user_id = ?;"""

    @staticmethod
    def database_get_by_id():
        return """SELECT id, database_name, user_id, host_id FROM databases WHERE id = ?;"""

    @staticmethod
    def database_get_by_name():
        return """SELECT id, database_name, user_id, host_id FROM databases WHERE database_name = ?;"""

    @staticmethod
    def database_insert():
        return """INSERT INTO databases (database_name, user_id, host_id) VALUES (?, ?, ?);"""

    @staticmethod
    def database_update():
        return """UPDATE databases SET database_name = ?, user_id = ?, host_id = ? WHERE id = ?;"""

    @staticmethod
    def database_delete():
        return """DELETE FROM databases WHERE id = ?;"""

    # Database Users Queries
    @staticmethod
    def database_user_get_by_id():
        return """SELECT id, database_id, database_username, connections
            FROM database_users
            WHERE id = ?;"""

    @staticmethod
    def database_user_get_by_name():
        return """SELECT id, database_id, database_username, connections
            FROM database_users
            WHERE database_username = ?;"""

    @staticmethod
    def database_user_insert():
        return """INSERT INTO database_users (database_id, database_username, connections) VALUES (?, ?, ?);"""

    @staticmethod
    def database_user_update():
        return """UPDATE database_users SET database_username = ?, connections = ? WHERE id = ?;"""


    @staticmethod
    def database_user_delete():
        return """DELETE FROM database_users WHERE id = ?;"""

