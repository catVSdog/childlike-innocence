from applications.auth.login_service import login_manager
from applications.auth.urls import urlpattern


def init_app(app):
    app.register_blueprint(urlpattern)
    login_manager.init_app(app)
