""" Cortex is responsible for high level logistical management of the data.

Once decisions have been made, processes are written to the database.
Once database details are written delegation down to the Nerv cells are
administered.

"""

from sassy.cortex.app import app
from sassy.cortex.config import DevelopmentConfig, ProductionConfig, TestingConfig
from sassy.utils.database.db import DatabaseConn

db = DatabaseConn()

