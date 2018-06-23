from flask import jsonify, Blueprint
from sassy.cortex.app import app

manage_users = Blueprint('manage_users', __name__)


@manage_users.route("/")
def index():
    return jsonify({'Manage_Users': __name__})
