import sqlite3

from sassy.cortex import app
from sassy.utils.database.sqlite import queries
from sassy.utils import errors

DATABASE = app.config.get('DATABASE')

query = queries.SqliteQueries()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def handler():
    try:
        db_conn = sqlite3.connect(DATABASE)
        db_conn.row_factory = dict_factory
        return db_conn
    except Exception as e:
        msg = f"Unable to connect to {DATABASE}"
        raise errors.DatabaseConnectionError(msg, e)


def create_sqlite_db():
    conn = handler()
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


def check_if_exists():
    conn = handler()
    output = conn.execute(query.check_if_exists())
    if len(output.fetchall()) > 0:
        return True
    return False
