from flask_migrate import Migrate


def init_app(app):
    from applications.auth.models import User
    from applications.blog.models import Blog
    from database_manger.db import db

    migrate_manager = Migrate()
    migrate_manager.init_app(app, db)
