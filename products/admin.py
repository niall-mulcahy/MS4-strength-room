from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'recurring'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'product',
        'full_name',
        'order_total',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
