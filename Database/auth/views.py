from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from . import auth_blueprint
from .models import db, User, Role

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # Implement user registration logic

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Implement user login logic
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token})