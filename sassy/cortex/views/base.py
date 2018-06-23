from flask import Blueprint, jsonify
from sassy.cortex.app import app
from sassy.utils import logger
from ..views import admin, databases, resources, users, websites
from sassy.utils import tools


log = logger.logger

api = Blueprint('api', __name__, template_folder='templates')
app.register_blueprint(admin.admin, url_prefix='/api/admin')
app.register_blueprint(databases.databases, url_prefix='/api/databases')
app.register_blueprint(resources.resources, url_prefix='/api/resources')
app.register_blueprint(users.users, url_prefix='/api/users')
app.register_blueprint(websites.websites, url_prefix='/api/websites')


@app.route('/')
def index():
    return 'Hello World!'


@api.route("/")
def api_index():
    return jsonify({'API Submodules': tools.discover_folders(__file__)})
