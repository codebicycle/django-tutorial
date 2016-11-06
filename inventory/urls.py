from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='inventory-index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
]
