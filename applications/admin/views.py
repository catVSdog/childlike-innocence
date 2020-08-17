from flask import jsonify
from flask_restful import Resource


class UserResource(Resource):
    """用户信息"""

    @staticmethod
    def get(user_id):
        return jsonify({'message': user_id})


class UserListResource(Resource):
    """用户列表信息"""

    @staticmethod
    def get():
        return jsonify({'message': 'ok'})
