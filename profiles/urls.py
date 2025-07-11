# profiles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('users/', views.user_list, name='user_list'), 
    path('submit/', views.submit_profile, name='submit_profile'), 
]

