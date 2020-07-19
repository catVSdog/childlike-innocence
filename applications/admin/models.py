from flask_login import UserMixin
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text)
from sqlalchemy.orm import relationship

from applications.admin.password_handler import Argon2Handler
from database.db import BaseModel


class User(UserMixin, BaseModel):
    username = Column(String(255), unique=True, nullable=False)
    profile_picture = Column(Text)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    last_login = Column(DateTime)
    role_id = Column(Integer, ForeignKey('role.id'))
    validated = Column(Boolean, default=False)

    def __str__(self):
        return f'<User: {self.username}>'

    password_handler = Argon2Handler()

    def set_password(self, row_password):
        self.password = self.password_handler.encode(row_password)

    def check_password(self, row_password):
        return self.password_handler.verify(row_password, self.password)


class Role(BaseModel):
    name = Column(String(50), unique=True, nullable=True)
    color = Column(String(20), unique=True, nullable=True)
    user = relationship('User', backref='role', lazy=True)

    def __str__(self):
        return f'<Role: {self.name}>'
