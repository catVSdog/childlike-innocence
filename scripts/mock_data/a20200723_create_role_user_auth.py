from applications import app
from applications.admin.models import Role, User, BasicAuth

app_context = app.app_context()
app_context.push()
from database.db import db

normal = Role(name='普通用户', color='green', is_default_role=True,
              permissions=1, description='普通权限')

admin = Role(name='管理员', color='blue',
             permissions=8, description='管理员权限')

zhangsan = User(nicknanme='zhangsan', about_me='i am zhangsan',
                role=normal)

lisi = User(nicknanme='lisi', about_me='i am lisi',
            role=admin)

zhangsan_auth = BasicAuth(username='zhangsan',
                          password='123', user=zhangsan)
lisi_auth = BasicAuth(username='lisi', password='123', user=lisi)

db.session.add(normal)
db.session.add(admin)
db.session.add(zhangsan)
db.session.add(lisi)
db.session.add(zhangsan_auth)
db.session.add(lisi_auth)
db.session.commit()
