from flask import Blueprint
from flask_restful import Api

from applications.blog.views import BlogListResource, BlogResource

blog_bp = Blueprint('backend_blog', __name__, url_prefix='/backend_blog')

rest_api = Api()
rest_api.init_app(blog_bp)
rest_api.add_resource(BlogListResource, '/blog/')
rest_api.add_resource(BlogResource, '/blog/<blog_id>')
