from django.shortcuts import render
from .data import products, eletronicos, jeweleries, men_clothing, women_clothing


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
