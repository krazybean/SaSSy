from flask import jsonify, Blueprint
from sassy.cortex.app import app

providers = Blueprint('providers', __name__)


@providers.route("/")
def index():
    return jsonify({'Providers': __name__})
