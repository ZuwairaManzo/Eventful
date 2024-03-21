from flask import jsonify

from . import analytics_blueprint
from .models import db, EventAnalytics
from events.models import Event

@analytics_blueprint.route('/<int:event_id>', methods=['GET'])
def get_event_analytics(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'Event not found'}), 404

    event_analytics = EventAnalytics.query.filter_by(event_id=event_id).first()
    if not event_analytics:
        return jsonify({'message': 'No analytics data found for this event'}), 404

    return jsonify({
        'event_id': event_id,
        'total_attendees': event_analytics.total_attendees,
        'total_tickets_sold': event_analytics.total_tickets_sold
    }), 200