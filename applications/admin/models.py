from flask_login import UserMixin
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from applications.admin.password_handler import Argon2Handler
from database.db import BaseModel


class User(UserMixin, BaseModel):
    username = Column(String(255), unique=True, nullable=False)
    profile_picture = Column(Text)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    last_login = Column(DateTime)
    role_id = Column(Integer, ForeignKey('Role.id'))

    def __str__(self):
        return f'<User: {self.username}>'

    # store raw password
    _password = None

    def set_password(self, row_password):
        password_handler = Argon2Handler()
        self.password = password_handler.encode(row_password)
        self._password = row_password

    def check_password(self, row_password):
        pass


class Role(BaseModel):
    name = Column(String(50), unique=True, nullable=True)
    color = Column(String(20), unique=True, nullable=True)
    user = relationship('User', backref='role', lazy=True)

    def __str__(self):
        return f'<Role: {self.name}>'
