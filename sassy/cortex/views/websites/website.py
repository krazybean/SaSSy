from flask import jsonify, Blueprint
from sassy.cortex.app import app

website = Blueprint('website', __name__)


@website.route("/")
def index():
    return jsonify({'Website': __name__})
