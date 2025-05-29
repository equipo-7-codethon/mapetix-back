from app.controllers.supabase_controller import SupabaseController

class NotificationController:
    def __init__(self):
        self.supabase_controller = SupabaseController()


    def subscribe_category(self, user_id, category_id):
        try:
            supabase = self.supabase_controller.get_supabase_client()
            response = supabase.table('event_notification').insert({'user_id': user_id, 'category_id': category_id}).execute()
            return response
        except Exception as e:
            raise e
        

    def unsubscribe_category(self, user_id, category_id):
        try:
            supabase = self.supabase_controller.get_supabase_client()
            response = supabase.table('event_notification').delete().eq('user_id', user_id).eq('category_id', category_id).execute()
            return response
        except Exception as e:
            raise e
        

    def get_subscribed_categories(self, user_id):
        try:
            supabase = self.supabase_controller.get_supabase_client()
            response = supabase.table('event_notification').select('*').eq('user_id', user_id).execute()
            return response
        except Exception as e:
            raise e
        

    def insert_notification_token(self, user_id, token):
        try:
            supabase = self.supabase_controller.get_supabase_client()
            response = supabase.table('user_token').insert({'user_id': user_id, 'token': token}).execute()
            return response
        except Exception as e:
            raise e
        

    def get_subscribed_user_token(self, category_id):
        try:
            supabase = self.supabase_controller.get_supabase_client()
            response = (
                supabase.from_('event_notification')
                .select('user_token(token)')
                .in_('category_id', category_id)
                .execute()
            )

            return response
        except Exception as e:
            raise e
        

    