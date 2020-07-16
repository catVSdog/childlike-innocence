from flask_restful import Resource


class BlogResource(Resource):
    """博客信息"""

    @staticmethod
    def get(blog_id):
        return {'message': blog_id}


class BlogListResource(Resource):
    """博客列表信息"""

    @staticmethod
    def get():
        return {'message': 'ok'}
