from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text)
from sqlalchemy.orm import backref, relationship

from applications.admin.password_handler import Argon2Handler
from database.db import BaseModel


class User(UserMixin, BaseModel):
    __tablename__ = 'user'
    nicknanme = Column(String(30), nullable=False, default='神秘用户')
    about_me = Column(String(255), nullable=True)
    profile_picture = Column(Text, nullable=True)
    last_login = Column(DateTime, default=datetime.now())
    role_id = Column(Integer, ForeignKey('role.id'))

    def __str__(self):
        return f'<User: {self.nicknanme}>'


class BasicAuth(BaseModel):
    __tablename__ = 'basic_auth'
    username = Column(String(10), unique=True)
    mobile = Column(String(11), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(100), nullable=False)
    email_is_validated = Column(Boolean, default=False)
    mobile_is_validated = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('basic', uselist=False), lazy=True)

    def __str__(self):
        return f'<BasicAuth: {self.username or self.mobile or self.email}'

    password_handler = Argon2Handler()

    def set_password(self, row_password):
        self.password = self.password_handler.encode(row_password)

    def check_password(self, row_password):
        return self.password_handler.verify(row_password, self.password)


class Oauth2Auth(BaseModel):
    __tablename__ = 'oauth2_auth'
    third_type = Column(Integer)  # 1.weibo 2.weixin
    auth_name = Column(String(255), unique=True)
    auth_token = Column(String(255), unique=True)
    is_validated = Column(Boolean, default=False)
    expires = Column(Integer)  # 时间戳
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('oauth', uselist=False), lazy=True)

    def __str__(self):
        return f'<OAuth2: {self.third_type}-{self.auth_name}'


class Role(BaseModel):
    __tablename__ = 'role'
    name = Column(String(50), unique=True, nullable=True)
    color = Column(String(20), unique=True, nullable=True)
    is_default_role = Column(Boolean, default=False)  # 动态配置某条记录是否为默认
    permissions = Column(Integer)
    description = Column(String(255))  # 描述角色权限
    user = relationship('User', backref='role', lazy=True)

    def __str__(self):
        return f'<Role: {self.name}-{self.description}>'
