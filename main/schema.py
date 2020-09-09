import graphene

from laptops.schema import Query as laptopQuery
from laptops.schema import Mutation as laptopMutation


class Query(laptopQuery, graphene.ObjectType):
    pass


class Mutation(laptopMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(Query, mutation=Mutation)