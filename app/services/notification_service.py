from app.controllers.notification_controller import NotificationController
from app.controllers.supabase_controller import SupabaseController
import requests

supabase_controller = SupabaseController()
EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"

class NotificationService:
    def __init__(self, notification_controller: NotificationController):
        self.notification_controller = notification_controller


    def subscribe_category(self, user_id, category_id):
        try:
            response = self.notification_controller.subscribe_category(user_id, category_id)
            return response
        except Exception as e:
            raise e
        

    def unsubscribe_category(self, user_id, category_id):
        try:
            response = self.notification_controller.unsubscribe_category(user_id, category_id)
            return response
        except Exception as e:
            raise e
        

    def get_subscribed_categories(self, user_id):
        try:
            response = self.notification_controller.get_subscribed_categories(user_id)
            response = supabase_controller.processresponseNoDF(response)
            return response
        except Exception as e:
            raise e
        

    def insert_notification_token(self, user_id, token):
        try:
            response = self.notification_controller.insert_notification_token(user_id, token)
            return response
        except Exception as e:
            raise e
        

    def notify_users(self, event):
        category_id = event['category_id']
        tokens = self.get_subscribed_user_token(category_id)
        if tokens:
            self.send_notifications(tokens, "Nuevo evento disponible", f"{event['title']} en {event['category']}")

            
    def get_subscribed_user_token(self, category_id):
        try:
            response = self.notification_controller.get_subscribed_user_token(category_id)
            return response
        except Exception as e:
            raise e


    def send_notifications(self, tokens, title, message):
        for token in tokens:
            payload = {
                "to": token,
                "sound": "default",
                "title": title,
                "body": message
            }
            requests.post(EXPO_PUSH_URL, json=payload)                         


    