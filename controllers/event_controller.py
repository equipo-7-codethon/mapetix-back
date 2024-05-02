from flask import request,jsonify
from controllers.supabase_controller import SupabaseController
from algoritmobueno import recommend_events_for_user

class EventController:

    def __init__(self):
        self.supabase_controller = SupabaseController()

    ### GET - /events
    def get_events(self, jwt_token):
        supabase = self.supabase_controller.get_supabase_client()
        userjwt_id = self.supabase_controller.GetUserIdFromjwt(jwt_token)
        events_by_user = supabase.table('event').select('*').eq('user_id', userjwt_id).execute()
        
        user_id = GetUserID(request)

        events = recommend_events_for_user(user_id)

         #aplicar filtro de ubicacion
        
        #aplicar filtro por horas


        # Convertimos los objetos Event a diccionarios antes de jsonify
        events_dict = [event.__dict__ for event in events]
        
        return jsonify(events_dict)     
