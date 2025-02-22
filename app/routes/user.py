from flask import jsonify, request
from app.controllers.supabase_controller import SupabaseController


supabase_controller = SupabaseController()

class UserView:

    def get_user_email_from_jwt():
        try:
            jwt_token = request.headers.get('Authorization')
            user_email = supabase_controller.GetUserEmailFromjwt(jwt_token)
            print(user_email)
            return jsonify(user_email)
        except Exception as e:
            return None