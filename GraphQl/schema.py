#ROOT SCHEMA
import graphene
from Client.schema import *

class RootQuery(clientQuery,ProductQuery,graphene.ObjectType):
    pass

class RootMutation(ClientMutation,ProductMutation,graphene.ObjectType):
    pass
schema=graphene.Schema(query=RootQuery,mutation=RootMutation)