from django.db import models

# Create your models here.
#Define a client profile model that includes basic details about a client

class products(models.Model):
    product_name=models.CharField(max_length=20,default="Skeleton")
    product_type=models.CharField(max_length=20,default="Watch")
    product_origin=models.CharField(max_length=20,default="Casio")

    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name_plural='Products'


class client_Profile(models.Model):
    name=models.CharField(max_length=50)
    membership_level=models.CharField(max_length=20,default="Regular")
    email=models.EmailField(max_length=20)
    client_description=models.TextField(max_length=200)
    preffered_product=models.ForeignKey(products)

    def __str__(self):
        return self.name


