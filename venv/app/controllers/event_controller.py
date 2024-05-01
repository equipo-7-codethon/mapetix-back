from flask import request,jsonify
from app.services import EventService

class EventController:
    def __init__(self):
        self.event_service = EventService()
    ### GET - /events
    def get_events(self, request):
        jwt_token = request.headers.get('Authorization')
        if not jwt_token:
            return jsonify({'error': ' Token JWT no proporcionado'}),401
        
        user_id = decode_jwt_token(jwt_token)
        events = self.event_service.get_events(user_id)

        # Convertimos los objetos Event a diccionarios antes de jsonify
        events_dict = [event.__dict__ for event in events]
        
        return jsonify(events_dict)
