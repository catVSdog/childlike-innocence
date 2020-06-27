from applications.admin.login_service import login_manager
from applications.admin.urls import urlpattern


def init_app(app):
    app.register_blueprint(urlpattern)
    # login_manager.init_app(app)
