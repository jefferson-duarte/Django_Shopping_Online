from django.contrib import messages
from django.shortcuts import render, redirect
from .data import products, eletronicos, jeweleries, men_clothing, women_clothing  # noqa: E501
from django.urls import reverse
from . models import ProductDB
from django.contrib.auth.decorators import login_required


@login_required(
    login_url='register_users:login_user',
    redirect_field_name='next'
)
def home(request):
    product_price = []

    for product in products:
        price = f"{product['price']:.2f}".replace('.', ',')
        product_price.append(price)

    return render(
        request,
        'client/pages/home.html', {
            'all_products': zip(products, product_price),
        }
    )


@login_required(
    login_url='register_users:login_user',
    redirect_field_name='next'
)
def product_detail(request, id):
    pdt_details = products[id-1]
    price = f"{pdt_details['price']:.2f}".replace('.', ',')

    return render(
        request,
        'client/pages/product_detail.html',
        {
            'pdt_details': pdt_details,
            'price': price,
        }
    )


@login_required(
    login_url='register_users:login_user',
    redirect_field_name='next'
)
def electronics(request):
    electronicos_price = []

    for electronic in eletronicos:
        price = f"{electronic['price']:.2f}".replace('.', ',')
        electronicos_price.append(price)

    return render(
        request,
        'client/pages/electronics.html',
        {
            'all_electronics': zip(eletronicos, electronicos_price)
        })


@login_required(
    login_url='register_users:login_user',
    redirect_field_name='next'
)
def jewelery(request):
    jeweleries_price = []

    for jewelery in jeweleries:
        price = f"{jewelery['price']:.2f}".replace('.', ',')
        jeweleries_price.append(price)

    return render(
        request,
        'client/pages/jewelery.html',
        {
            'all_jeweleries': zip(jeweleries, jeweleries_price)
        })


@login_required(
    login_url='register_users:login_user',
    redirect_field_name='next'
)
def men_clothings(request):
    men_clothing_price = []

    for men in men_clothing:
        price = f"{men['price']:.2f}".replace('.', ',')
        men_clothing_price.append(price)

    return render(
        request,
        'client/pages/men_clothing.html',
        {
            'all_men_clothing': zip(men_clothing, men_clothing_price)
        })


@login_required(
    login_url='register_users:login_user',
    redirect_field_name='next'
)
def women_clothings(request):
    women_clothing_price = []

    for women in women_clothing:
        price = f"{women['price']:.2f}".replace('.', ',')
        women_clothing_price.append(price)

    return render(
        request,
        'client/pages/women_clothing.html',
        {
            'all_women_clothing': zip(women_clothing, women_clothing_price)
        })


@login_required(
    login_url='register_users:login_user',
    redirect_field_name='next'
)
def product_cart(request, id):
    product = products[id-1]

    cart = ProductDB(
        product['id'],
        product['title'],
        product['price'],
        product['description'],
        product['category'],
    )

    cart.save()

    messages.success(request, 'Product added to cart')

    return redirect(reverse('products:product_detail', kwargs={'id': id}))
