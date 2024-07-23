import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import User, session

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return session.query(User).all()

schema = graphene.Schema(query=Query)
