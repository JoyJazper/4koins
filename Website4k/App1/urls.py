
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'StoresApp1'

urlpatterns = [
    #/app1/
    path('', views.index, name='index'),

    #/app1/storeId/
    path('<int:storeID>/', views.ProductPanel, name='ProductPanel' ),
    #path('1/', views.ProductPanel, name='ProductPanel' )

    path('cart/', views.Cart, name='CartPanel' )

]
