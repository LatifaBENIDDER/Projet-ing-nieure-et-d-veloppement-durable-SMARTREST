from re import template
from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='SR-Home'),
    path('commande/', views.commande, name='SR-commande'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='SR-Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='SR-Logout'),
]
