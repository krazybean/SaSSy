from flask import jsonify, Blueprint
from sassy.cortex.app import app

hosts = Blueprint('hosts', __name__)


@hosts.route("/")
def index():
    return jsonify({'Hosts': __name__})
