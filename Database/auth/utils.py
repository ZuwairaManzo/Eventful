from flask_jwt_extended import get_jwt_identity

from .models import User, Role

def get_current_user():
    user_id = get_jwt_identity()
    return User.query.get(user_id)

def get_user_role(user):
    return user.role.name

def is_event_creator(user):
    return get_user_role(user) == 'creator'

def is_attendee(user):
    return get_user_role(user) == 'attendee'