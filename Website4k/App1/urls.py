
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #/app1/
    path('', views.index,name = 'index' ),

    #/app1/storeId
    path('<int:storeID>/',views.ProductPanel, name = 'ProductPanel' )
]
