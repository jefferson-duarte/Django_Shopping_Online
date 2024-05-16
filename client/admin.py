from django.contrib import admin
from .models import ProductDB


@admin.register(ProductDB)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'description',
        'category',
    ]
