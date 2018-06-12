import sqlite3

from sassy.cortex import app
from sassy.utils.database.sqlite import queries

DATABASE = app.config.get('DATABASE')


def handler():
    try:
        db_conn = sqlite3.connect(DATABASE)
        return db_conn
    except Exception:
        app.logger.error(f"Unable to connect to f{DATABASE}")


def create_sqlite_db():
    conn = handler()
    query = queries.SqliteQueries()
    conn.execute(query.create_table_users())
    conn.execute(query.create_table_websites())
    conn.execute(query.create_table_ssl())
    conn.execute(query.create_table_cms())
    conn.execute(query.create_table_roles())
    conn.execute(query.create_table_databases())
    conn.execute(query.create_table_database_users())
    conn.execute(query.create_table_hosts())
    conn.execute(query.create_table_providers())
    conn.execute(query.create_table_devicetype())
    conn.execute(query.create_table_device_attributes())
    conn.commit()
