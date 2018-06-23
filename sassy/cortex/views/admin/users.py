from flask import jsonify, Blueprint
from sassy.cortex.app import app

admin_users = Blueprint('admin_users', __name__)


@admin_users.route("/")
def index():
    return jsonify({'Users': __name__})


@admin_users.route('/test')
def testing():
    return jsonify({'test': 'pass'})
