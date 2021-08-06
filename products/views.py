from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Product
from .forms import NewOrderForm
import stripe


def products(request):
    """ A view to return all products available on the site """

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_checkout(request, product_id):
    """ A view to return clicked on product to allow purchase """

    product = get_object_or_404(Product, pk=product_id)
    order_form = NewOrderForm()

    stripe_total = product.price

    context = {
        'product': product,
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J9omdJq4HTAYf7lueZYAvtrZobGmqSRbBHLdQHtOLAKNn86VA2lNidxBAKf092yMIL4jVvUPdigVYUg18OxRSae00TDu9dySF',
        'client_secret': 'Test client',
    }

    return render(request, 'products/product_checkout.html', context)
