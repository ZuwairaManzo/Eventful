from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EventAnalytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    total_attendees = db.Column(db.Integer, nullable=False, default=0)
    total_tickets_sold = db.Column(db.Integer, nullable=False, default=0)