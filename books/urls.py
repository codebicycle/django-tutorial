from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.list_books, name='books'),
    url(r'^authors/$', views.AuthorList.as_view(), name='authors'),
]
