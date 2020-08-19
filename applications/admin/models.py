from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        SmallInteger, String, Text)
from sqlalchemy.orm import backref, relationship

from applications.admin.password_handler import Argon2Handler
from applications.common.base_model import BaseModel
from database.db import db


class User(UserMixin, BaseModel):
    __tablename__ = 'user'
    __bind_key__ = 'admin'  # if not set this property, use default database, SQLALCHEMY_DATABASE_URI's value
    nicknanme = Column(String(30), nullable=False, default='神秘用户')
    about_me = Column(String(255), nullable=True)
    profile_picture = Column(Text, nullable=True)
    joined_time = Column(DateTime, default=datetime.utcnow)
    lastest_login = Column(DateTime, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship('Role', backref=backref('user'), lazy=True)

    def __repr__(self):
        return f'<User: {self.nicknanme}>'

    def update_lastest_login(self):
        self.lastest_login = datetime.utcnow()
        db.session.add(self)


class BasicAuth(BaseModel):
    __tablename__ = 'basic_auth'
    __bind_key__ = 'admin'
    username = Column(String(10), unique=True)
    mobile = Column(String(11), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(100), nullable=False)
    email_is_validated = Column(Boolean, default=False)
    mobile_is_validated = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('basic', uselist=False), lazy=True)

    def __repr__(self):
        return f'<BasicAuth: {self.username or self.mobile or self.email}'

    password_handler = Argon2Handler()

    def set_password(self, row_password):
        self.password = self.password_handler.encode(row_password)

    def check_password(self, row_password):
        return self.password_handler.verify(row_password, self.password)


class Oauth2Auth(BaseModel):
    __tablename__ = 'oauth2_auth'
    __bind_key__ = 'admin'
    third_type = Column(Integer)  # 1.weibo 2.weixin
    auth_name = Column(String(50), unique=True)
    auth_token = Column(String(100))
    is_validated = Column(Boolean, default=False)
    expires = Column(Integer)  # 时间戳
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('oauth', uselist=False), lazy=True)

    def __repr__(self):
        return f'<OAuth2: {self.third_type}-{self.auth_name}'


class Role(BaseModel):
    __tablename__ = 'role'
    __bind_key__ = 'admin'
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))  # 描述角色权限
    color = Column(String(20), unique=True, nullable=False)
    is_default_role = Column(Boolean, default=False)  # 动态配置某条记录是否为默认
    permission_id = Column(Integer, ForeignKey('permission.id'))
    permission = relationship('Permission', backref=backref("role", uselist=False))

    def __repr__(self):
        return f'<Role: {self.name}-{self.description}>'

    def __str__(self):
        return 'Role'


class Permission(BaseModel):
    __tablename__ = 'permission'
    __bind_key__ = 'admin'
    description = Column(String(100), nullable=False)
    bit_number = Column(SmallInteger, nullable=False, unique=True)
    code = Column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return f'<Permission: {self.description}>'

    def __str__(self):
        return 'Permission'
