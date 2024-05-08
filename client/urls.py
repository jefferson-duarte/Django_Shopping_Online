from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/electronics/', views.electronics, name='electronics'),
    path('category/jeweleries/', views.jewelery, name='jeweleries'),
    path('category/men_clothing/', views.men_clothings, name='men_clothing'),
    path('category/women_clothing/', views.women_clothings, name='women_clothing'),  # noqa:E501
]
