from django.shortcuts import render
from .data import products
from django.http import HttpResponse


def home(request):
    product_price = []

    for product in products:
        price = f"{product['price']:.2f}".replace('.', ',')
        product_price.append(price)

    return render(
        request,
        'client/pages/home.html', {
            'all_products': zip(products, product_price),
            'products': products,
            'product_price': product_price
        }
    )


def electronics(request):
    return render(request, 'client/pages/electronics.html')


def products_list(request):
    return HttpResponse('Nada')
    # return render(request, 'client/pages/products.html', {
    #     'products': products,
    # })
