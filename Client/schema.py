
from graphene import AbstractType,Field,Node,String,Int,ClientIDMutation
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from .models import *
# creating an object that can be accessed from the graphql endpoint
#the node classes are equivalent to the serializers in REST framework
class clientNode(DjangoObjectType):
    class Meta:
        model=client_Profile
        interfaces=(Node,)
        # can do read_only fields, exclude_fields,and so on
        filter_fields={'name':['icontains'],'membership_level':['icontains']}

class ProductNode(DjangoObjectType):
    class Meta:
        model=products
        interfaces = (Node,)
        filter_fields = ['product_name', 'product_type']


class clientQuery(AbstractType):# abstract so that they can be inherited in the root schema
    single_client=Node.Field(clientNode)
    client=DjangoFilterConnectionField(clientNode)

class ProductQuery(AbstractType):
    single_product=Node.Field(ProductNode)# used when querying for a
    #  specific item using an ID
    products=DjangoFilterConnectionField(ProductNode)
#--------------------MUTATIONS------------

class NewProduct(ClientIDMutation):
    Pnode = Field(ProductNode) # the node that will be holding the data

    class Input: # appears as suggestions in the graphiQl interface in the input set
        name = String()


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        temp = products(
            product_name=input.get('name'),# from the input set, derive the
            #value assigned to name and assign to product_name( actual value in the model)

        )
        temp.save()
        return NewProduct(Pnode=temp) #return an object of type NewProduct which is a node

class NewClient(ClientIDMutation):
    client = Field(clientNode)

    class Input:
        name = String()
        client_description=String()
        email=String()
        product=String()

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        client = client_Profile(
            name=input.get('name'),
            email=input.get('email'),
            client_description=input.get('client_description'),
            preffered_product=products.objects.get(product_name=input.get('product'))
        )
        client.save()
        return NewClient(client=client)


class ClientMutation(AbstractType):
    new_client = NewClient.Field()

class ProductMutation(AbstractType):
    new_product = NewProduct.Field()