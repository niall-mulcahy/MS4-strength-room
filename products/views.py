from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import NewOrderForm


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

    context = {
        'product': product,
        'order_form': order_form,
    }

    return render(request, 'products/product_checkout.html', context)
