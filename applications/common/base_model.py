from datetime import datetime

from sqlalchemy import Column, DateTime, Integer

from database.db import db


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        try:
            db.session.commit()
        except Exception as exec:
            db.session.rollback()
            raise exec
        return instance

    def update(self, **kwargs):
        try:
            for key, value in kwargs.items():
                if not hasattr(self, key):
                    raise AttributeError(f"'{self}' object has no attribute '{key}'")
                setattr(self, key, value)
            db.session.commit()
        except Exception as exec:
            db.session.rollback()
            raise exec

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        if self.id is None:
            db.session.add(self)
            db.session.commit()
        else:
            db.session.commit()
