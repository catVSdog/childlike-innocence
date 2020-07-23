# pylint:disable=unused-import
from flask_migrate import Migrate


def init_app(app):
    from applications.admin.models import BasicAuth, Oauth2Auth, Role, User
    from applications.blog.models import Post
    from database.db import db


    migrate_manager = Migrate()
    migrate_manager.init_app(app, db)
