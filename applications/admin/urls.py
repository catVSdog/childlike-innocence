from applications.admin.views import IndexView, RegisterView
from flask import Blueprint

urlpattern = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

urlpattern.add_url_rule('/register', view_func=RegisterView.as_view('register'))
urlpattern.add_url_rule('/index', view_func=IndexView.as_view('index'))
