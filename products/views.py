from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .models import Product, Order
from profiles.models import UserProfile

from .forms import NewOrderForm, NewProductForm
from profiles.forms import UserProfileForm

import stripe
import datetime


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        product_name = request.session['product_name']
        print(product_name)
        stripe.PaymentIntent.modify(pid, metadata={
            'Product': product_name,
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def products(request):
    """ A view to return all products available on the site """

    if request.user.is_authenticated:

        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'products/products.html', context)
    else:
        products = Product.objects.all()

        context = {
            'products': products
        }
        messages.info(request, 'To proceed with a purchase on this site you will need to register for an account or login!')
        return render(request, 'products/products.html', context)


@login_required
def product_checkout(request, product_id):
    """ A view to return clicked on product to allow purchase """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    product = get_object_or_404(Product, pk=product_id)
    # Used this session variable to send it to the stripe meta data
    request.session['product_name'] = product.name
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
        return redirect(
            reverse('checkout_success', args=[order[0]]))
    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = NewOrderForm(initial={
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                })
            except profile.DoesNotExist:
                order_form = NewOrderForm()
        else:
            order_form = NewOrderForm()

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
    profile = UserProfile.objects.get(user=request.user)
    save_info = request.session.get('save_info')
    product = request.session.get('product')
    order = get_object_or_404(Order, order_number=order_number)
    membership_site = get_object_or_404(Product, id=1)
    print(membership_site)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

    # Save the user's info
    if order.product == membership_site:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_town_or_city': order.town_or_city,
            'default_postcode': order.postcode,
            'default_county': order.county,
            'default_country': order.country,
            'is_member': True,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    else:
        if profile.is_member:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_postcode': order.postcode,
                'default_county': order.county,
                'default_country': order.country,
                'is_member': True,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
        else:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_postcode': order.postcode,
                'default_county': order.county,
                'default_country': order.country,
                'is_member': False,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    order_date = order.date
    print(order_date)
    resub_date = order_date + datetime.timedelta(days=7)

    template = 'products/checkout_success.html'

    context = {
        'product': product,
        'order': order,
        'save_info': save_info,
        'resub_date': resub_date,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    if request.user.is_superuser:
        template = 'products/add_product.html'
        new_product_form = NewProductForm()

        if request.method == "POST":
            name = request.POST.get("name")
            description = request.POST.get("description")
            price = request.POST.get("price")
            Product.objects.get_or_create(
                name=name,
                description=description,
                price=price,
                recurring=False,
            )
            messages.success(request, f'You have added a new product {name}')
            return redirect(reverse('products'))
        else:
            context = {
                'new_product_form': new_product_form,
            }
            return render(request, template, context)
    else:
        messages.error(request, 'Whoops! Looks like you are not logged in as the admin user!')
        return redirect(reverse('home'))


def delete_product(request, product_id):
    if request.user.is_superuser:
        template = 'products/delete_product.html'
        product = get_object_or_404(Product, pk=product_id)

        if request.method == "POST":
            product.delete()
            messages.info(request, 'This product has been deleted')
            return redirect(reverse('products'))

        context = {
            'product': product
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Whoops! Looks like you are not logged in as the admin user!')
        return redirect(reverse('home'))
