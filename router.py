from flask import Blueprint
from app_view import app_view,AppViews


class Router:
    def __init__(self, app):
        self.app = app

        # Blueprints para los endpoints de planes
        plan_bp = Blueprint('plan', __name__)
        plan_bp2 = Blueprint('plan2', __name__)
        plan_bp.add_url_rule('/plans', view_func=AppViews.get_plans)
        plan_bp2.add_url_rule('/plan/<int:id>', view_func=AppViews.get_plan)
        self.app.register_blueprint(plan_bp)
        self.app.register_blueprint(plan_bp2)

        # Blueprint para eliminar un plan
        plan_delete_bp = Blueprint('plan_delete', __name__)
        plan_delete_bp.add_url_rule('/plan/<int:id>', view_func=AppViews.delete_plan)
        self.app.register_blueprint(plan_delete_bp)

        # Blueprint para modificar un plan
        plan_modify_bp = Blueprint('plan_modify', __name__)
        plan_modify_bp.add_url_rule('/plan/<int:id>', view_func=AppViews.modify_plan)
        self.app.register_blueprint(plan_modify_bp)

        # Blueprint para crear un plan
        plan_create_bp = Blueprint('plan_create', __name__)
        plan_create_bp.add_url_rule('/plan', view_func=AppViews.create_plan)
        self.app.register_blueprint(plan_create_bp)

        # Blueprint para obtener eventos
        event_bp = Blueprint('event', __name__)
        event_bp.add_url_rule('/events', view_func=AppViews.get_events)
        self.app.register_blueprint(event_bp)

        # Blueprint para obtener los planes por usuario
        plan_user_bp = Blueprint('plan_user', __name__)
        plan_user_bp.add_url_rule('/plans', view_func=AppViews.get_plans_by_user)
        self.app.register_blueprint(plan_user_bp)