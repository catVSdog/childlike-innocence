from flask import Blueprint
from flask_restful import Api

from applications.admin.views import UserListResource, UserResource

admin_bp = Blueprint('backend_admin', __name__, url_prefix='/backend_admin')

rest_api = Api()
rest_api.init_app(admin_bp)
rest_api.add_resource(UserListResource, '/user/')
rest_api.add_resource(UserResource, '/user/<user_id>')
