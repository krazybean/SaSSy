from flask import Blueprint, jsonify
from sassy.cortex.app import app
from sassy.utils import tools
from .website import website


websites = Blueprint('websites', __name__)
app.register_blueprint(website, url_prefix='/api/websites/website')


@websites.route("/")
def index():
    return jsonify({'Websites Submodules': tools.discover_files(__file__)})
