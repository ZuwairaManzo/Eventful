from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def init_cache(app):
    cache.init_app(app, config={'CACHE_TYPE': 'simple