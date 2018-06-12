from sassy.utils import logger
from sassy.utils import errors
from sassy.utils.database import sqlite


class DatabaseConn(object):

    def __init__(self):
        self.conn = None
        self.conn = self.connect()
        self.build_initial_data()

    def connect(self):
        try:
            db = sqlite.handler()
            self.conn = db
        except Exception as e:
            msg = "Error building connection object"
            raise errors.DatabaseConnectionError(msg, e)

    def build_initial_data(self):
        if not sqlite.check_if_exists():
            sqlite.create_sqlite_db()
            sqlite.preseed_db()


