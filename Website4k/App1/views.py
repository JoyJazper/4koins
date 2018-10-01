from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Users
from .models import Stores
from .models import Products
from .models import OrdersList
from .models import OrderData

# Create your views here.
def index(request):
    listUser = Users.objects.all()
    listStores = Stores.objects.all()
    context = {
        'Stores': listStores,
    }
    for store in listStores:
        url = '/app1/'+ str(store.storeID) + '/'
        html += '<a href="'+url+'">'+ store.storeName+'</a><br />'
    return render(request, 'App1/index.html', context)

def ProductPanel(request, storeID):
    StoreD = get_object_or_404(Stores, pk=storeID)
    return render(request, 'App1/productdetails.html', {'StoreD': StoreD})
    #return HttpResponse("<h1> This is the Products Panel of :" + str(storeID) + "</h1>")

def AddToCart(request, productID):
    listproducts = Products.objects.all()
    listOrders = OrdersList.objects.all()
    length = (listOrders.length())+1
    product = get_object_or_404(Products, pk=productID)
    p = OrderData(
        storeID = product.storeID,
        userID = "SomeOne",
        orderID = length,
        orderAmount = "1000",
        status = "ordered!"
    )
    p.save()
    return render(request, 'App1/productdetails.html', {'StoreD': product.storeID})

def Cart(request, orderID):
    listOrders = OrdersList.objects.all()
    products = get_object_or_404(OrdersList)
    return render(request, 'App1/cart.html', products)