from database.db import init_app as db_init_app
from database.migrate import init_app as mg_init_app


def init_app(app):
    db_init_app(app)
    mg_init_app(app)
