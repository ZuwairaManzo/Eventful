from flask import jsonify, request
import requests

from . import api_blueprint

@api_blueprint.route('/events', methods=['POST'])
def create_event():
    # Forward the request to the Event Management Service
    event_service_url = "http://event-service/events/create"
    headers = {
        'Authorization': request.headers.get('Authorization')
    }
    response = requests.post(event_service_url, headers=headers, json=request.get_json())
    return jsonify(response.json()), response.status_code

# Add more routes to forward requests to different microservices