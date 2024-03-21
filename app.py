from flask import Flask
from flask_jwt_extended import JWTManager

from auth import auth_blueprint
from events import events_blueprint
from qrcodes import qrcodes_blueprint
from sharing import sharing_blueprint
from notifications import notifications_blueprint
from analytics import analytics_blueprint
from api_gateway import api_blueprint

from utils.config import Config
from utils.common import init_db, init_cache

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(events_blueprint)
app.register_blueprint(qrcodes_blueprint)
app.register_blueprint(sharing_blueprint)
app.register_blueprint(notifications_blueprint)
app.register_blueprint(analytics_blueprint)
app.register_blueprint(api_blueprint)

init_db(app)
init_cache(app)

if __name__ == '__main__':
    app.run()
    
    
    # app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventful.db'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    creator_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'location': self.location,
            'creator_id': self.creator_id
        }

@app.route('/api/v1/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)