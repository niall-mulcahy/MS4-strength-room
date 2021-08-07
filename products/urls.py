from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<product_id>', views.product_checkout, name='product_checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]
