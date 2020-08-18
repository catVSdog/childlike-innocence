from sqlalchemy import Column, String

from applications.common.base_model import BaseModel


class Post(BaseModel):
    __tablename__ = 'post'
    __bind_key__ = 'blog'
    title = Column(String(20), unique=True, nullable=False)
