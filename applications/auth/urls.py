from applications.auth.views import RegisterView
from flask import Blueprint

urlpattern = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

urlpattern.add_url_rule('/register', view_func=RegisterView.as_view('register'))
