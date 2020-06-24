from database_manger.db import db


class Blog(db.Model):
    __bind_key__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    label = db.Column(db.Integer)

    def __repr__(self):
        return f'<Blog {self.name}>'
