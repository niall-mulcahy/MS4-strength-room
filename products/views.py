from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .models import Product, Order
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

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    product = get_object_or_404(Product, pk=product_id)
    order_form = NewOrderForm()

    stripe_total = round(product.price * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        street_address1 = request.POST.get("street_address1")
        street_address2 = request.POST.get("street_address2")
        town_or_city = request.POST.get("town_or_city")
        county = request.POST.get("county")
        country = request.POST.get("country")
        postcode = request.POST.get("postcode")
        if order_form.is_valid:
            order = Order.objects.get_or_create(
                product=product,
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                street_address1=street_address1,
                street_address2=street_address2,
                town_or_city=town_or_city,
                county=county,
                country=country,
                postcode=postcode,
                order_total=product.price
            )
            request.session['save_info'] = 'save-info' in request.POST
            print(order[1])
            return redirect(
                reverse('checkout_success', args=[order[0]]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    context = {
        'product': product,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'products/product_checkout.html', context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    product = get_object_or_404(Product, order.product)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    template = 'products/checkout_success.html'

    context = {
        'order': order,
        'product': product,
    }

    return render(request, template, context)
