from django.urls import path
from .views import view_cart
from cart import views as cart_views

urlpatterns = [
    path('',view_cart,name='view_cart'),
    path('cart/add/<int:product_id>', cart_views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', cart_views.cart_remove, name='cart_remove'),
    path('cart/trashbin_product/<int:product_id>', cart_views.trashbin_product, name='trashbin_product'),
    path('cart', cart_views.cart_detail, name='cart_detail'),
    path('thankyou/<int:order_id>', cart_views.thank_you, name='thank_you'),
    ]