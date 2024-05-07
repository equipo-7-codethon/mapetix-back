from flask import Blueprint, jsonify, request
from controllers.event_controller import EventController
from controllers.plan_controller import PlanController
from auth_middleware import require_authentication
from controllers.supabase_controller import SupabaseController

app_view = Blueprint('app-view', __name__)

event_controller = EventController()
plan_controller = PlanController()
supabase_controller = SupabaseController()

class AppViews:
     ### GET - /events
    @app_view.route('/events', methods=['GET'])
    @require_authentication
    def get_events():
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        user_location = request.args.get('userLocation')
        if not user_location:
            return jsonify({'error': 'No user location provided'}), 400
        if userjwt_id:
            events = event_controller.get_events(userjwt_id, user_location)
            return jsonify(events)
        return jsonify({'error': 'Usuario no válido'}), 401

    ### DELETE - /plan/:id    Elimina un plan (id = plan_id)
    @app_view.route('/plan/<int:id>', methods=['DELETE'])
    @require_authentication
    def delete_plan(id):
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        if userjwt_id:
            response = plan_controller.delete_plan(id)
            return jsonify(response)
        return jsonify({'error': 'Usuario no válido'}), 401

     # GET - /plan/:id   Devuelve un plan concreto de un usuario (id = plan_id)
    @app_view.route('/plan/<int:id>', methods=['GET'])
    @require_authentication
    def get_plan(id):
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        if userjwt_id:
            plan = plan_controller.get_plan(id)
            return jsonify(plan)
        return jsonify({'error': 'Usuario no válido'}), 401

    ### PUT - /plan/:id  Modificar plan
    @app_view.route('/plan/<int:id>', methods=['PUT'])
    @require_authentication
    def modify_plan(id):
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        plan_data = request.get_json()
        if not plan_data:
            return jsonify({"error": "No data provided"}), 400
        if userjwt_id:
            response = plan_controller.modify_plan(id, plan_data)
            return jsonify(response)
        return jsonify({'error': 'Usuario no válido'}), 401

    # POST - /plan      Crea un plan para un usario (JWT)
    @app_view.route('/plan', methods=['POST'])
    @require_authentication
    def create_plan():
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        if userjwt_id:
            response = plan_controller.create_plan(userjwt_id)
            return jsonify(response)
        return jsonify({'error': 'Usuario no válido'}), 401

    # GET - /plans      Obtiene los planes ya hecho por el usuario (JWT)
    @app_view.route('/plans', methods=['GET'])
    @require_authentication
    def get_plans_by_user():
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        if userjwt_id:
            plans = plan_controller.get_plans_by_user(userjwt_id)
            return jsonify(plans)
        return jsonify({'error': 'Usuario no válido'}), 401
