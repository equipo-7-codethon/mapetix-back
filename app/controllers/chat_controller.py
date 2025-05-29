from app.controllers.supabase_controller import SupabaseController

class ChatController:
    def __init__(self):
        self.supabase_controller = SupabaseController()

    def insert_message(self, message, event_id, user_id, jwt_token):
        try:
            supabase = self.supabase_controller.get_supabase_client()
            user = self.supabase_controller.GetUserEmailFromjwt(jwt_token)
            response = supabase.table('message').insert({'message': message, 'event_id': event_id, 'user': user}).execute()
            return response
        except Exception as e:
            raise e
        

    def get_messages(self, event_id):
        try:
            supabase = self.supabase_controller.get_supabase_client()
            response = supabase.table('message').select('*').eq('event_id', event_id).order('created_at', desc=True).limit(10).execute()
            response.data = response.data[::-1]
            return response
        except Exception as e:
            raise e
        
