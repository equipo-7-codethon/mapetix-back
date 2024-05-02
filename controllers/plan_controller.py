from flask import request,jsonify
from supabase_controller import SupabaseController
import json

class PlanController:
    def __init__(self):
        self.supabase_controller = SupabaseController()
    
    # GET - /plans      Obtiene los planes ya hecho por el usuario (JWT)
    def get_plans_by_user(self, jwt_token):
        supabase = self.supabase_controller.get_supabase_client()
        userjwt_id = self.supabase_controller.GetUserIdFromjwt(jwt_token)
        plans_by_user = supabase.table('plan').select('*').eq('user_id', userjwt_id).execute()

    # GET - /plan/:id   Devuelve un plan concreto de un usuario (id = plan_id)
    def get_plan(self,id):
        supabase = self.supabase_controller.getsupabase_client()
        #obtener el plan
        plan = supabase.table('plan').select('*').eq('plan_id', id).execute()
        #obtener los eventos de un plan
        event_ids = supabase.table('plan_event').select('event_id').eq('plan_id',id).execute()

        #obtener los detalles de cada evento
        events = [
            supabase.table('events')
                .select('*')
                .eq('id', event_id['id'])
                .execute()
            for event_id in event_ids
        ]

        formatted_events = self.processresponseNoDF(events)
    


    # POST - /plan      Crea un plan para un usario (JWT)


    ### PUT - /plan/:id   Modifica el plan de un usuario (id = plan_id)



    ### DELETE - /plan/:id    Elimina un plan (id = plan_id)
    def delete_plan(self,id):
        supabase = self.supabase_controller.get_supabase_client()
        eliminaPlan = supabase.table('plan').delete().eq('plan_id',id).execute()


    def formatPlan(self,plan):
        supabase = self.supabase_controller.get_supabase_client()
        events_ids = supabase.table('plan_event').select('event_id').eq('plan_id',plan).execute()
        
        events = [
            supabase.table('events')
                .select('*')
                .eq('id', event_id['id'])
                .execute()
            for event_id in events_ids
        ]

        plan["events"] = self.processresponseNoDF(events)
        return plan

    def processresponseNoDF(response):
        try:
            # Obtener los datos en formato JSON utilizando el método model_dump_json()
            response_json = response.model_dump_json()

            # Convertir los datos en un diccionario
            response_dict = json.loads(response_json)

            # Acceder a los datos de las valoraciones
            valorations_data = response_dict['data']

            return valorations_data

        except Exception as e:
            print("Error:", e)
            return None
