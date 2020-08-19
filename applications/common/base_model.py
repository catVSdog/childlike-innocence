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

    @classmethod
    def update(cls, instance, **kwargs):
        # todo: may be need query first
        try:
            for key, value in kwargs.items():
                if not hasattr(instance, key):
                    raise AttributeError(f"'{instance}' object has no attribute '{key}'")
                instance.key = value
            db.session.commit()
        except Exception as exec:
            db.session.rollback()
            raise exec
        return instance

    @classmethod
    def delete(cls, instance):
        # todo: may be need query first
        db.session.delete(instance)

    def save(self, *args, **kwargs):
        # todo: like Django, object method, used by add/update
        pass
