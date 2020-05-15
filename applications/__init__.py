import os

from flask import Flask

from applications import auth
from applications import blog
from conf import db


def create_app(config=None):
    app = Flask(__name__)

    if 'FLASK_CONFIG' in os.environ:
        app.config.from_object(os.environ('FLASK_CONFIG'))
    else:
        app.config.from_object('conf.settings')

    if config is not None:
        # config 中的键均需为大写格式,否则会被忽略
        app.config.from_mapping(**config)

    db.init_app(app)
    auth.init_app(app)
    blog.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
