from flask import jsonify, request
from app.controllers.chat_controller import ChatController
from app.controllers.supabase_controller import SupabaseController

chat_controller = ChatController()
supabase_controller = SupabaseController()

class ChatView:

    def get_event_messages(id):
        try:
            jwt_token = request.headers.get('Authorization')
            user_email = supabase_controller.GetUserEmailFromjwt(jwt_token)
            if user_email:
                messages = chat_controller.get_messages(id)
                messages = supabase_controller.processresponseNoDF(messages)
                return jsonify(messages)
        except Exception as e:
            return None
        
    
    def insert_message():
        try:
            jwt_token = request.headers.get('Authorization')
            userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
            if userjwt_id:
                data = request.get_json()
                if not data:
                    return jsonify({'error': 'Datos no enviados'}), 400

                message = data.get('Message')
                event_id = data.get('EventId')

                chat_controller.insert_message(message, event_id, userjwt_id, jwt_token)
                return jsonify({'message': 'Mensaje enviado'})
        except Exception as e:
            raise e