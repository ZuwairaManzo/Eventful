from flask_apscheduler import APScheduler
import requests
from datetime import datetime, timedelta

scheduler = APScheduler()

def scheduled_notifications():
    # Fetch upcoming events from the Event Management Service
    upcoming_events = fetch_upcoming_events()

    # Send notifications for upcoming events
    for event in upcoming_events:
        event_id = event['id']
        event_date = datetime.fromisoformat(event['date'])
        event_time = datetime.fromisoformat(event['time']).time()
        event_datetime = datetime.combine(event_date, event_time)

        # Calculate the time difference between the current time and the event time
        time_diff = event_datetime - datetime.now()

        # Send notifications based on the time difference
        if time_diff < timedelta(days=1):
            send_notification(event_id, 'day_before')
        elif time_diff < timedelta(weeks=1):
            send_notification(event_id, 'week_before')
        # Add more conditions for different notification intervals

def fetch_upcoming_events():
    # Make a request to the Event Management Service to fetch upcoming events
    upcoming_events_url = "http://event-service/events/upcoming"
    response = requests.get(upcoming_events_url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def send_notification(event_id, notification_type):
    # Implement logic to send notifications for the specified event and notification type
    # You can use email, push notifications, SMS, or other methods
    print(f"Sending {notification_type} notification for event {event_id}")