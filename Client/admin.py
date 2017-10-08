from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(client_Profile)
admin.site.register(products)