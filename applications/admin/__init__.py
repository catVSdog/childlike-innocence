from applications.admin.login_service import login_manager
from applications.admin.urls import admin_bp


def init_app(app):
    app.register_blueprint(admin_bp)

    # login_manager.init_app(app)
