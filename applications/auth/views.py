from flask.views import MethodView


class RegisterView(MethodView):
    methods = ['GET', 'POST']

    @staticmethod
    def get():
        return "get"
