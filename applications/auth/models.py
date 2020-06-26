from applications.auth.password_handler import Argon2Handler
from database.db import BaseModel
from flask_login import UserMixin
from sqlalchemy import Column, DateTime, String


class User(UserMixin, BaseModel):
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    last_login = Column(DateTime)

    def __repr__(self):
        return f'<User {self.username}>'

    # store raw password
    _password = None

    def set_password(self, password):
        password_handler = Argon2Handler()
        self.password = password_handler.encode(password)
        self._password = password
