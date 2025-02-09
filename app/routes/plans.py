from flask import jsonify, request
from app.controllers.plan_controller import PlanController
from app.controllers.supabase_controller import SupabaseController


plan_controller = PlanController()
supabase_controller = SupabaseController()

class PlanView:

    def get_plans():
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        if userjwt_id:
            plans = plan_controller.get_plans_by_user(userjwt_id)
            return jsonify(plans)
        else:
            # Si el ID de usuario no existe, devolver un mensaje de error
            return jsonify({'error': 'Usuario no autorizado'}), 401


    def get_plan(id):
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        #if not user_location:
        #    return jsonify({'error':'No user location provided'}),400
        if userjwt_id:
            user_location = request.args.get('userLocation')
            user_location = tuple(map(float, user_location.split(',')))
            plan =  plan_controller.get_plan(id,user_location)
            return jsonify(plan)
        else:
            # Si el ID de usuario no existe, devolver un mensaje de error
            return jsonify({'error': 'Usuario no autorizado'}), 401
    

    def rate_event(id):
        try:
            jwt_token = request.headers.get('Authorization')
            userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
            if userjwt_id:

                data = request.get_json()
                if not data:
                    return jsonify({'error': 'Datos no enviados'}), 400

                nota = data.get('Nota')
                description_val = data.get('Description')

                plan =  plan_controller.valorate_event(id,userjwt_id,nota,description_val)
                return jsonify(plan)
            else:
                # Si el ID de usuario no existe, devolver un mensaje de error
                return jsonify({'error': 'Usuario no autorizado'}), 401
        except Exception as e:
            # Manejar la excepción y devolver un mensaje de error adecuado
            print(jsonify({'error': str(e)}))


    def create_plan():
        try:
            # Obtener el token JWT de la solicitud (suponiendo que está en el encabezado Authorization)
            jwt_token = request.headers.get('Authorization')
            userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
            if userjwt_id:
                user_location = request.args.get('userLocation')
                user_location = tuple(map(float, user_location.split(',')))
                max_distance = request.args.get('maxDistance')
                max_distance = float(max_distance)
                target_date = request.args.get('TargetDate')
                max_price = request.args.get('maxPrice')
                max_price = int(max_price)
                plans = plan_controller.create_plan(userjwt_id,user_location,max_distance,target_date,max_price)
                return jsonify(plans)
            else:
                # Si el ID de usuario no existe, devolver un mensaje de error
                return jsonify({'error': 'Usuario no autorizado'}), 401
            
        except Exception as e:
            # Manejar la excepción y devolver un mensaje de error adecuado
            return jsonify({'error': str(e)}), 400
        


    
        


    
        


    
        


    