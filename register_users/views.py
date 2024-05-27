from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


def register(request):
    if request.method == 'GET':
        return render(request, 'register_users/register_home.html')

    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if not password == confirm_password:
            messages.add_message(
                request,
                constants.ERROR,
                'Password is not equal.'
            )
            return redirect(reverse('register_users:register'))

        user = User.objects.filter(
            username=username
        )

        if user.exists():
            messages.add_message(
                request,
                constants.ERROR,
                'Username already exist.'
            )
            return redirect(reverse('register_users:register'))

        user_email = User.objects.filter(
            email=email
        )

        if user_email.exists():
            messages.add_message(
                request,
                constants.ERROR,
                'Email already exist.'
            )
            return redirect(reverse('register_users:register'))

    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password
    )

    user.save()
    messages.add_message(
        request,
        constants.SUCCESS,
        'User created with success!'
    )

    return redirect(reverse('register_users:login_user'))


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            messages.add_message(
                request,
                constants.SUCCESS,
                'Login success!'
            )

            return redirect(reverse('products:home'))

        messages.add_message(
            request,
            constants.ERROR,
            'Credentials invalid.'
        )
    return render(request, 'register_users/login_register.html')


@login_required(
    login_url='register_users:login_user',
    redirect_field_name='next'
)
def logout_user(request):
    if not request.POST:
        messages.error(request, 'Invalid logout request.')
        return redirect(reverse('register_users:login_user'))

    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Invalid logout user.')
        return redirect(reverse('register_users:login_user'))

    auth.logout(request)

    messages.success(request, 'Logged out successfully.')
    return redirect(reverse('register_users:login_user'))
