from django.urls import path
from . import views
from django.conf import settings

 

urlpatterns = [
     path('owner', views.owner, name='owner'),
     path('login', views.login.as_view(), name='login'),
    #  path('assign', views.assign, name='assign'),
     path('logout', views.homepage, name='homepage'),

]
     
    