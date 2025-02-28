from flask import Blueprint
from app.routes.plans import  PlanView
from app.routes.events import EventView
from app.routes.scrap import ScrapView
from app.routes.chat import ChatNamespace  # Importamos el chat
from flask_socketio import SocketIO
from app.middleware.auth_middleware import require_authentication
from app.routes.chatview import ChatView
from app.routes.user import UserView
from app.routes.notification import NotificationView
from app.services.notification_service import NotificationService
from app.controllers.notification_controller import NotificationController

notification_controller = NotificationController()
notification_service = NotificationService(notification_controller)
notification_view = NotificationView(notification_service)

class Router:
    def __init__(self, app):
        self.app = app
        self.socketio = SocketIO(app)

        plan_bp = Blueprint('plans', __name__)
        events_bp = Blueprint('events', __name__ )
        scrap_bp = Blueprint('scrap', __name__ )
        chat_bp = Blueprint('chat', __name__)
        user_bp = Blueprint('user', __name__)
        notification_bp = Blueprint('notification', __name__)

        plan_bp.add_url_rule('/plans', view_func=require_authentication(PlanView.get_plans), methods=['GET'], endpoint='get_plans_by_user')
        plan_bp.add_url_rule('/plan/<int:id>', view_func=require_authentication(PlanView.get_plan), methods=['GET'], endpoint='get_plan_by_id')
        plan_bp.add_url_rule('/plan/rate/<int:id>', methods=['POST'], view_func=require_authentication(PlanView.rate_event), endpoint='rate_event')
        plan_bp.add_url_rule('/plan', view_func=require_authentication(PlanView.create_plan), methods= ['GET'], endpoint='create_plan')

        events_bp.add_url_rule('/allevents', view_func=require_authentication(EventView.get_all_events), methods=['GET'], endpoint='get_all_events')
        events_bp.add_url_rule('/event/<int:id>', view_func=require_authentication(EventView.get_event), methods=['GET'], endpoint='get_event_by_id')
        events_bp.add_url_rule('/event/rate/<int:id>', view_func=require_authentication(EventView.get_event_rate), methods = ['GET'], endpoint='get_event_rate')
        events_bp.add_url_rule('/event/categories', view_func=require_authentication(EventView.get_categories), methods = ['GET'], endpoint='get_events_categories')

        scrap_bp.add_url_rule('/scrap', view_func=ScrapView.do_scrap, methods=['GET'], endpoint='do_scrap')

        chat_bp.add_url_rule('/messages/<int:id>', view_func=require_authentication(ChatView.get_event_messages), methods=['GET'], endpoint='get_event_messages')
        chat_bp.add_url_rule('/messages', view_func=require_authentication(ChatView.insert_message), methods=['POST'], endpoint='insert_message')

        user_bp.add_url_rule('/user/email', view_func=require_authentication(UserView.get_user_email_from_jwt), methods=['GET'], endpoint='get_user_email_from_jwt')

        notification_bp.add_url_rule('/notification/subscribe', view_func=require_authentication(notification_view.subscribe_category), methods=['POST'], endpoint='subscribe_category')
        notification_bp.add_url_rule('/notification/unsubscribe', view_func=require_authentication(notification_view.unsubscribe_category), methods=['DELETE'], endpoint='unsubscribe_category')
        notification_bp.add_url_rule('/notification/subscribed', view_func=require_authentication(notification_view.get_subscribed_categories), methods=['GET'], endpoint='get_subscribed_categories')   
        notification_bp.add_url_rule('/notification/token', view_func=require_authentication(notification_view.insert_notification_token), methods=['POST'], endpoint='insert_notification_token') 


        self.app.register_blueprint(plan_bp)
        self.app.register_blueprint(events_bp)
        self.app.register_blueprint(scrap_bp)
        self.app.register_blueprint(chat_bp)
        self.app.register_blueprint(user_bp)
        self.app.register_blueprint(notification_bp)

        self.socketio.on_namespace(ChatNamespace('/chat'))