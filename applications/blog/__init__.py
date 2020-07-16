from applications.blog.urls import blog_bp


def init_app(app):
    app.register_blueprint(blog_bp)
