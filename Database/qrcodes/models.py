from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False, unique=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)