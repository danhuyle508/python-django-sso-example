from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.login, name='login'),
    path('auth', views.auth, name='auth'),
    path('auth/callback', views.auth_callback, name='auth_callback'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/sso/static/images/favicon.ico')),
    
]
