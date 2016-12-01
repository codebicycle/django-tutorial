from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^register/$', views.UserRegistrationView.as_view(),
        name='user_registration'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),
]
