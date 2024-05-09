from flask import request,jsonify
from algoritmobueno import recommend_events_for_user
from controllers.supabase_controller import SupabaseController
from controllers.plan_controller import PlanController
import math

class EventController:

    def __init__(self):
        self.supabase_controller = SupabaseController()
        self.plan_controller = PlanController()

    ### GET - /events
    def get_events(self, user_id,ubicacion):

        events = recommend_events_for_user(user_id)
        events = self.supabase_controller.table('event').select('*').in_('id',events).execute()
        events = self.plan_controller.processresponseNoDF(events)
        #aplicar filtro por horas
        

        #aplicar filtro de ubicacion
        events_ubicado = self.ordenarEventosDistancia(events,ubicacion)
        
        return jsonify(events_ubicado)

    #POST - /valoration
    def valorate_events(self,event_id,jwt_token,nota,description_val):
        supabase = self.supabase_controller.get_supabase_client()
        userjwt_id = self.supabase_controller.GetUserIdFromjwt(jwt_token)
        #event = supabase.table('event').select('id').eq('id' , event_id).execute()
        supabase.table('valoration_event').insert({'event_id' : event_id, 'score' : nota, 'description_valoration' : description_val, 'auth_user_id' : userjwt_id}).execute()

    #ordena los eventos por distancia segun el array de eventos y la ubicacion del usuario
    def ordenarEventosDistancia(self,events,ubicacion):
        #extraer latitud y longitud de la ubicacion del usuario
        try:
            lat, lon = map(float, ubicacion.split(','))
        except ValueError:
            return jsonify({'error': 'Invalid user location format'}), 400

        events.sort(key=lambda event: self.haversine_distance(lat, lon, events['coord_y'], events['coord_x']))
        return events     
    

    #calcular distancia entre dos puntos segun latitud y longitud
    @staticmethod
    def haversine_distance(lat1, lon1, lat2, lon2):
        # Convertir grados en radianes
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.asin(math.sqrt(a))
    
        # Radio de la Tierra en km
        r = 6371
        return c * r
    
    