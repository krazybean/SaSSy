from flask import jsonify, Blueprint
from sassy.cortex.app import app
from flasgger.utils import swag_from

admin_users = Blueprint('admin_users', __name__)


@admin_users.route("/")
@swag_from('admin_user.yml')
def index():
    return jsonify({'Users': __name__})


@admin_users.route('/test')
def testing():
    return jsonify({'test': 'pass'})
