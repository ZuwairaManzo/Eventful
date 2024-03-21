from flask import Blueprint

sharing_blueprint = Blueprint('sharing', __name__, url_prefix='/sharing')

from . import views