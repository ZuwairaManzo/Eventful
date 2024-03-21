from flask import jsonify, request
import requests

from . import sharing_blueprint
from .integrations import share_on_platform

@sharing_blueprint.route('/share', methods=['POST'])
def share_event():
    data = request.get_json()
    event_id = data.get('event_id')
    social_platform = data.get('social_platform')

    # Fetch event details from the Event Management Service
    event_details = fetch_event_details(event_id)

    if event_details is None:
        return jsonify({'message': 'Event not found'}), 404

    # Share event details on the specified social platform
    share_on_platform(social_platform, event_details)

    return jsonify({'message': 'Event shared successfully'}), 200

def fetch_event_details(event_id):
    # Make a request to the Event Management Service to fetch event details
    event_url = f"http://event-service/events/{event_id}"
    response = requests.get(event_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None