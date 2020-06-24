from flask import Flask


def create_app(config=None, flask=Flask('childlike-innocence')):
    from applications import auth, blog
    import database_manger

    app = flask

    env_settings_map = {
        'development': 'conf.settings',
        'production': 'conf.settings_prd'
    }
    app.config.from_object(env_settings_map.get(app.env, 'conf.settings'))

    if config is not None:
        # config 中的键均需为大写格式,否则会被忽略
        app.config.from_mapping(**config)

    database_manger.init_app(app)

    auth.init_app(app)
    blog.init_app(app)

    @app.route('/hello/')
    def hello():
        return "hello"

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
