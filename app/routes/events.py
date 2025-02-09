from flask import jsonify, request
from app.controllers.plan_controller import PlanController
from app.controllers.supabase_controller import SupabaseController
from datetime import datetime


plan_controller = PlanController()
supabase_controller = SupabaseController()

class EventView:

    def get_all_events():
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        if userjwt_id:
            price = request.args.get('price', type=float)
            valoration = request.args.get('valoration', type=float)
            category = request.args.get('category', type=int)
            target_date = datetime.today().strftime('%Y-%m-%d')
            allevents = plan_controller.filter_events_by_date(target_date, price, valoration, category)
            #allevents_2 = plan_controller.filter_events_all(allevents, price, valoration, category)
            contador = 0
            for event in allevents:
                contador +=1
            print(contador)
            return jsonify(allevents)
        else:
            # Si el ID de usuario no existe, devolver un mensaje de error
            return jsonify({'error': 'Usuario no autorizado'}), 401
        

    def get_event(id):
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        #if not user_location:
        #    return jsonify({'error':'No user location provided'}),400
        if userjwt_id:
            event =  plan_controller.get_event_by_id(id)
            print("hola")
            return jsonify(event)
        else:
            # Si el ID de usuario no existe, devolver un mensaje de error
            return jsonify({'error': 'Usuario no autorizado'}), 401
        

    def get_event_rate(id):
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)

        if userjwt_id:
            event =  plan_controller.get_event_user_rated(id, userjwt_id)
            return jsonify(event)
        else:
            # Si el ID de usuario no existe, devolver un mensaje de error
            return jsonify({'error': 'Usuario no autorizado'}), 401
        

    def get_categories():
        try:
            categories = plan_controller.get_categories()
            return jsonify(categories)
        except Exception as e:
            # Manejar la excepción y devolver un mensaje de error adecuado
            return jsonify({'error': str(e)}), 500