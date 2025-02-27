from flask import jsonify, request
from app.services.notification_service import NotificationService
from app.controllers.supabase_controller import SupabaseController

supabase_controller = SupabaseController()

class NotificationView():
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service


    def subscribe_category(self):
        try:
            jwt_token = request.headers.get('Authorization')
            userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
            if userjwt_id:
                data = request.get_json()
                if not data:
                    return jsonify({'error': 'Datos no enviados'}), 400

                category_id = data.get('CategoryId')

                self.notification_service.subscribe_category(userjwt_id, category_id)
                return jsonify({'message': f'Subscripción a la categoria {category_id} exitosa'})
        except Exception as e:
            raise e
        

    def unsubscribe_category(self):
        try:
            jwt_token = request.headers.get('Authorization')
            userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
            if userjwt_id:
                data = request.get_json()
                if not data:
                    return jsonify({'error': 'Datos no enviados'}), 400

                category_id = data.get('CategoryId')

                self.notification_service.unsubscribe_category(userjwt_id, category_id)
                return jsonify({f'message': f'Se eliminó la subscripción a la categoria {category_id} exitosamente'})
        except Exception as e:
            raise e
        

    def get_subscribed_categories(self):
        try:
            jwt_token = request.headers.get('Authorization')
            userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
            if userjwt_id:
                response = self.notification_service.get_subscribed_categories(userjwt_id)
                return jsonify(response)
        except Exception as e:
            raise e
        

    def insert_notification_token(self):
        try:
            jwt_token = request.headers.get('Authorization')
            userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
            if userjwt_id:
                data = request.get_json()
                if not data:
                    return jsonify({'error': 'Datos no enviados'}), 400

                token = data.get('Token')

                self.notification_service.insert_notification_token(userjwt_id, token)
                return jsonify({'message': 'Token registrado'})
        except Exception as e:
            raise e