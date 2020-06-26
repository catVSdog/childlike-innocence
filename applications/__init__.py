from flask import Flask


def create_app(config=None, flask=Flask('childlike-innocence')):
    from applications import auth, blog
    import database

    env_settings_map = {
        'development': 'conf.settings',
        'production': 'conf.settings_prd'
    }
    flask.config.from_object(env_settings_map.get(flask.env, 'conf.settings'))

    if config is not None:
        # config 中的键均需为大写格式,否则会被忽略
        flask.config.from_mapping(**config)

    database.init_app(flask)
    auth.init_app(flask)
    blog.init_app(flask)

    return flask


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
