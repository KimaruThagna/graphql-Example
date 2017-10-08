A BASIC GRAPHQL EXAMPLE\

#########################LOGIN CREDENTIALS ##################################
to log in to django admin,
username:admin
password:graphql123

The simple project demonstrates use of graphene and graphql in a django project.
major libraries used include
graphene-django
django-graphiql
django-filter
and thus, do pip install for each

on the web graphiql interface, try the following examples which will do retreivals

{
  singleClient(id:"Y2xpZW50Tm9kZTox")
  {
    name
    clientDescription
  }
}

  client
  {
    edges
    {
      node
      {
        name
        clientDescription
        email
        prefferedProduct
        {
          productName
          productType
        }
      }
    }
  }
}


{
  products
  {
    edges
    {
      node
      {
        productName
        productType
        productOrigin
        clientProfileSet
        {
          edges
          {
            node
            {
              name
            }
          }
        }
      }
    }
  }
}

Mutations for adding a record is also supported and can be done as

mutation
{
  newProduct(input:{name:"myNew product"})
  {
    Pnode
    {
      productName
    }
  }
}
################the above query adds a new prroduct in the products model

