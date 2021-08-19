from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('wh/', webhook, name='webhook'),
    path('<product_id>/product_checkout', views.product_checkout, name='product_checkout'),
    path('<product_id>/delete_product', views.delete_product, name='delete_product'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
]
