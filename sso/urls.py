from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url


urlpatterns = [
    path('', views.login, name='login'),
    path('auth', views.auth, name='auth'),
    path('auth/callback', views.auth_callback, name='auth_callback'),
]
