from flask import Blueprint
from app.routes.plans import  PlanView
from app.routes.events import EventView
from app.routes.scrap import ScrapView
from app.middleware.auth_middleware import require_authentication


class Router:
    def __init__(self, app):
        self.app = app
        plan_bp = Blueprint('plans', __name__)
        events_bp = Blueprint('events', __name__ )
        scrap_bp = Blueprint('scrap', __name__ )


        plan_bp.add_url_rule('/plans', view_func=require_authentication(PlanView.get_plans), methods=['GET'], endpoint='get_plans_by_user')
        plan_bp.add_url_rule('/plan/<int:id>', view_func=require_authentication(PlanView.get_plan), methods=['GET'], endpoint='get_plan_by_id')
        plan_bp.add_url_rule('/plan/rate/<int:id>', methods=['POST'], view_func=require_authentication(PlanView.rate_event), endpoint='rate_event')
        plan_bp.add_url_rule('/plan', view_func=require_authentication(PlanView.create_plan), methods= ['GET'], endpoint='create_plan')

        events_bp.add_url_rule('/allevents', view_func=require_authentication(EventView.get_all_events), methods=['GET'], endpoint='get_all_events')
        events_bp.add_url_rule('/event/<int:id>', view_func=require_authentication(EventView.get_event), methods=['GET'], endpoint='get_event_by_id')
        events_bp.add_url_rule('/event/rate/<int:id>', view_func=require_authentication(EventView.get_event_rate), methods = ['GET'], endpoint='get_event_rate')
        events_bp.add_url_rule('/event/categories', view_func=require_authentication(EventView.get_categories), methods = ['GET'], endpoint='get_events_categories')

        scrap_bp.add_url_rule('/scrap', view_func=ScrapView.do_scrap, methods=['GET'], endpoint='do_scrap')


        self.app.register_blueprint(plan_bp)
        self.app.register_blueprint(events_bp)