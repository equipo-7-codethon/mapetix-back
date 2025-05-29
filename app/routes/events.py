from flask import jsonify, request
from app.controllers.plan_controller import PlanController
from app.controllers.supabase_controller import SupabaseController
from datetime import datetime


plan_controller = PlanController()
supabase_controller = SupabaseController()

class EventView:

    def get_all_events():
        price = request.args.get('price', type=float)
        valoration = request.args.get('valoration', type=float)
        category = request.args.get('category', type=int)
        target_date = datetime.today().strftime('%Y-%m-%d')
        allevents = plan_controller.filter_events_by_date(target_date, price, valoration, category)
        contador = 0
        for event in allevents:
            contador +=1
        return jsonify(allevents)
        

    def get_event(id):
        event =  plan_controller.get_event_by_id(id)
        if event:
            return jsonify(event)
        else:
            return jsonify({'error': 'Event not found'}), 404
        

    def get_event_rate(id):
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        event =  plan_controller.get_event_user_rated(id, userjwt_id)
        if event:
            return jsonify(event)
        else:
            return jsonify({'error': 'Event not found'}), 404
        

    def get_categories():
        categories = plan_controller.get_categories()
        return jsonify(categories)