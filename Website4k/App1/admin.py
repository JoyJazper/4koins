from django.contrib import admin
from . models import Users, Stores, OrderData, OrdersList, Products
# Register your models here.

admin.site.register(Users)
admin.site.register(Stores)
admin.site.register(OrderData)
admin.site.register(OrdersList)
admin.site.register(Products)