from flask import Blueprint, jsonify, request
from controllers.plan_controller import PlanController
from auth_middleware import require_authentication
from auth_middleware import AuthMiddleware
from controllers.supabase_controller import SupabaseController


plan_view = Blueprint('plan-view', __name__)
plan_controller = PlanController()
supabase_controller = SupabaseController()
auth_middleware = AuthMiddleware()

class PlanView:
    @plan_view.route('/plans', methods=['GET'])
    @require_authentication  # Aplicar el middleware de autenticación
    def get_plans():
        # Obtener el token JWT de la solicitud (suponiendo que está en el encabezado Authorization)
        jwt_token = request.headers.get('Authorization')
        #session = supabase_controller.Prueba()

        # Obtener los planes del usuario utilizando el controlador de planes
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        print(userjwt_id)
        if auth_middleware.is_valid_token(userjwt_id):
            plans = plan_controller.get_plans_by_user(userjwt_id)   
            return jsonify(plans) 
        else:
            return jsonify({'error': 'No authorization token provided'}), 401

