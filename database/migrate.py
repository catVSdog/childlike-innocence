from flask_migrate import Migrate


def init_app(app):
    from applications.admin.models import User  # pylint:disable=unused-import
    from database.db import db


    migrate_manager = Migrate()
    migrate_manager.init_app(app, db)
