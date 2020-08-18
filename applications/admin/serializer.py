from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from applications.admin.models import BasicAuth, Oauth2Auth, Role, User


class UserSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True  # Whether to include foreign fields; defaults to False.


class BasicAuthSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = BasicAuth
        include_fk = True


class Oauth2AuthSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Oauth2Auth
        include_fk = True


class RoleSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk = True
