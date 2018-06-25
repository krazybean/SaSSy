from flask import Blueprint, jsonify
from flasgger.utils import swag_from
from sassy.cortex.app import app
from .users import admin_users
from sassy.utils import tools


admin = Blueprint('admin', __name__)
app.register_blueprint(admin_users, url_prefix='/api/admin/users')


@admin.route("/")
@swag_from('admin_base.yml')
def index():
    return jsonify({'Admin Submodules': tools.discover_files(__file__)})
