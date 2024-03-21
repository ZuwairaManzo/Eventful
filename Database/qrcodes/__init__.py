from flask import Blueprint

qrcodes_blueprint = Blueprint('qrcodes', __name__, url_prefix='/qrcodes')

from . import views, models