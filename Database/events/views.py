from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import events_blueprint
from .models import db, Event, Ticket
from auth.utils import is_event_creator

@events_blueprint.route('/create', methods=['POST'])
@jwt_required()
def create_event():
    current_user = get_jwt_identity()
    if not is_event_creator(current_user):
        return jsonify({'message': 'Unauthorized access'}), 403

    data = request.get_json()
    # Implement event creation logic

@events_blueprint.route('/<int:event_id>/register', methods=['POST'])
@jwt_required()
def register_event(event_id):
    current_user = get_jwt_identity()
    # Implement event registration logic