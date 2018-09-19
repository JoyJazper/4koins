from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users, Stores, Products, OrdersList, OrderData

# Create your views here.
def index(request):
    listStores = Stores.objects.all()
    html = ''
    template = loader.get_template('templates/App1/index.html')
    context = {
        'Stores': Stores,
    }
    for store in listStores:
        url = '/App1/'+ str(store.id) + '/'
        html += '<a href="'+url+'">'+ store.storeName+'</a><br />'
    return HttpResponse(template.render(context, request))

def ProductPanel(request, storeID):
    return HttpResponse("<h1> This is the Products Panel " + str(storeID) + "</h1>")