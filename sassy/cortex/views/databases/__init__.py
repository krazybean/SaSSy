from flask import Blueprint, jsonify
from sassy.cortex.app import app
from .mysql import mysql
from sassy.utils import tools


databases = Blueprint('databases', __name__)
app.register_blueprint(mysql, url_prefix='/api/databases/mysql')


@databases.route("/")
def index():
    return jsonify({'Database Submodules': tools.discover_files(__file__)})
