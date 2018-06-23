from flask import Blueprint, jsonify
from sassy.cortex.app import app
from sassy.utils import tools
from .manage_users import manage_users


users = Blueprint('users', __name__)
app.register_blueprint(manage_users, url_prefix='/api/users/manage_users')


@users.route("/")
def index():
    return jsonify({'Users Submodules': tools.discover_files(__file__)})
