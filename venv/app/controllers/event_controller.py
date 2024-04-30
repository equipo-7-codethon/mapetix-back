from flask import jsonify
from app.services import EventService

event_service = EventService()

class EventController:
    def get_events(self, request):
        user_location = request.args.get('userLocation')
        date = request.args.get('date')
        category = request.args.get('category')

        events = event_service.get_events(user_location, date, category)
        
        # Convertimos los objetos Event a diccionarios antes de jsonify
        events_dict = [event.__dict__ for event in events]
        
        return jsonify(events_dict)
