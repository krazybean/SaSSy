from flask import Blueprint, jsonify
from sassy.cortex.app import app
from sassy.utils import tools
from .containers import containers
from .virtualmachines import vms
from .hosts import hosts
from .providers import providers


resources = Blueprint('resources', __name__)
app.register_blueprint(containers, url_prefix='/api/resources/containers')
app.register_blueprint(vms, url_prefix='/api/resources/virtualmachines')
app.register_blueprint(hosts, url_prefix='/api/resources/hosts')
app.register_blueprint(providers, url_prefix='/api/resources/providers')


@resources.route("/")
def index():
    return jsonify({'Resource Submodules': tools.discover_files(__file__)})
