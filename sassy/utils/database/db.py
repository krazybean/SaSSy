# Database Connections here
from sassy.utils import logger
from sassy.utils.database.sqlite import queries


class DatabaseConn(object):

    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self, ):
        try:
            from sassy.utils.database.sqlite import handler
            db = handler()
            self.conn = db
        except Exception:
            logger.error("Error building connection object")

