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
    """
       This is the SaSSy API
       This base route will provide no additional functionality
       ---
       tags:
         - SaSSy API
       responses:
         200:
           description: SaSSy API
       """
    return 'SaSSy API'


@api.route("/")
def api_index():
    """
       SaSSy API Subdirectory
       Call this api to list the subroutes and methods available
       ---
       tags:
         - API Directory to provide guidance to sub-methods
       responses:
         500:
           description: Error parsing submodules
         200:
           description: API Submodules
           schema:
             id: api
             properties:
               response:
                 type: array
                 description: Methods available under the submodule scope
                 items:
                   type: string
                 default: {"API Submodules": ["databases", "resources", "admin", "users", "websites"]}

       """
    return jsonify({'API Submodules': tools.discover_folders(__file__)})
