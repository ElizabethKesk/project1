"""
Definition of urls for VXAPP.
"""

from django.urls import path 
from . import views 
from django.contrib import admin


urlpatterns = [
    path('', views.index,name='home'),
    path('home1/', views.home1,name='home1'),
    path('home2/', views.home2,name='home2'),
    path('home3/', views.home3,name='home3'),
    path('new-user', views.register,name ='new-user'),
    path('auth', views.login_auth,name='auth'),
    path('logout', views.logout_auth,name='exit'),
    path('profile', views.profile_views,name='profile'),
    path('update_user', views.update_profile_user,name='update-user'),
    path('admin', admin.site.urls,name='admin'), 
   
]

