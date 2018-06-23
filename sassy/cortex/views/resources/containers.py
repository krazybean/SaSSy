from flask import jsonify, Blueprint
from sassy.cortex.app import app

containers = Blueprint('containers', __name__)


@containers.route("/")
def index():
    return jsonify({'Containers': __name__})
