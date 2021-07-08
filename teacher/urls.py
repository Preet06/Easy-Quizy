from django.urls import path
from . import views
from django.contrib import admin
from .views import SignUpView
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .views import BlogCreateView
from django.urls import path,include


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('home2/', views.home2, name='home2'),
    path('home2/sett/', BlogCreateView.as_view(), name='sett'),

]