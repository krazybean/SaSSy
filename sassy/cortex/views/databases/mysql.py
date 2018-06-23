from flask import Blueprint, jsonify

mysql = Blueprint('mysql', __name__)

@mysql.route('/')
def index():
    return jsonify({'API Module': __name__})