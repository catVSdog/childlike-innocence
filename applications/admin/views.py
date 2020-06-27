from flask.views import MethodView


class RegisterView(MethodView):
    methods = ['GET', 'POST']

    @staticmethod
    def get():
        print("register")
        return 'hello'


class IndexView(MethodView):
    methods = ['GET']

    @staticmethod
    def get():
        return 'idex'
