from django.urls import path
from . import views

app_name = 'register_users'

urlpatterns = [
    path('register/', views.register, name='register'),
]
