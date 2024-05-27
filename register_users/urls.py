from django.urls import path
from . import views

app_name = 'register_users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]
