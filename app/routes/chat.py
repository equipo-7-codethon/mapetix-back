from flask_socketio import Namespace, emit, join_room, leave_room
from flask import request
from app.controllers.supabase_controller import SupabaseController

supabase_controller = SupabaseController()

class ChatNamespace(Namespace):

    def on_connect(self):
        print("Usuario conectado al chat")


    def on_disconnect(self):
        print("Usuario desconectado del chat")

    
    def on_join(self, data):
        jwt_token = request.headers.get('Authorization')
        userjwt_id = supabase_controller.GetUserIdFromjwt(jwt_token)
        if not userjwt_id:
            emit('error', {'message': 'Usuario no autorizado'}, broadcast=False)
            return

        room = data.get('room')
        join_room(room)
        emit('joined', {'user': userjwt_id, 'room': room}, room=room)
        print(f"Usuario {userjwt_id} se unió a la sala {room}")


    def on_leave(self, data):
        room = data.get('room')
        leave_room(room)
        print(f"Usuario dejó la sala {room}")


    def on_message(self, data):
        jwt_token = request.headers.get('Authorization')
        user_email = supabase_controller.GetUserEmailFromjwt(jwt_token)
        if not user_email:
            emit('error', {'message': 'Usuario no autorizado'}, broadcast=False)
            return

        message = data.get('message', '')
        room = data.get('room')

        print(f"Mensaje en sala {room}: {message}")
        emit('message', {'user': user_email, 'message': message}, room=room)
