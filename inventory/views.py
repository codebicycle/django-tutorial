from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<p>Inventory Index View</p>')

def item_detail(request, id):
    return HttpResponse('<p>item_detail view with id {}</p>'.format(id))
