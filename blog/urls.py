from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/$', views.NewBlogView.as_view(), name='new-blog'),
]
