from django.urls import path
from . import views

urlpatterns = [
    path('give_code', views.give_code, name='give_code'),
    path('search_bar', views.search_bar, name='search_bar'),
    path('final', views.final, name='final')
]