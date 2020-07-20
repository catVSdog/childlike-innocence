from flask_login import UserMixin
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text)
from sqlalchemy.orm import backref, relationship

from applications.admin.password_handler import Argon2Handler
from database.db import BaseModel


class User(UserMixin, BaseModel):
    nicknanme = Column(String(30), nullable=False, default='匿名用户')
    profile_picture = Column(Text)
    last_login = Column(DateTime)
    role_id = Column(Integer, ForeignKey('role.id'))

    def __str__(self):
        return f'<User: {self.nicknanme}>'


class BasicAuth(BaseModel):
    username = Column(String(255), unique=True)
    mobile = Column(String(11), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255), nullable=False)
    email_is_validated = Column(Boolean, default=False)
    mobile_is_validated = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('basic', uselist=False), lazy=True)

    password_handler = Argon2Handler()

    def set_password(self, row_password):
        self.password = self.password_handler.encode(row_password)

    def check_password(self, row_password):
        return self.password_handler.verify(row_password, self.password)


class OauthAuth(BaseModel):
    third_type = Column(Integer)
    auth_name = Column(String(255), unique=True)
    auth_token = Column(String(20), unique=True)
    is_validated = Column(Boolean, default=False)
    expires = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('oauth', uselist=False), lazy=True)


class Role(BaseModel):
    name = Column(String(50), unique=True, nullable=True)
    color = Column(String(20), unique=True, nullable=True)
    description = Column(String(255))  # 描述角色权限
    user = relationship('User', backref='role', lazy=True)

    def __str__(self):
        return f'<Role: {self.name}>'
