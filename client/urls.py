from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/electronics/', views.electronics, name='electronics'),
    path('products/', views.products_list, name='products'),
]
