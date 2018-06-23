from flask import jsonify, Blueprint
from sassy.cortex.app import app

vms = Blueprint('virtualmachines', __name__)


@vms.route("/")
def index():
    return jsonify({'VirtualMachines': __name__})
