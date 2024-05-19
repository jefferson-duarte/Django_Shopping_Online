from django.shortcuts import render


def register(request):
    return render(request, 'register_users/register_home.html')
