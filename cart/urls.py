from django.urls import path
from .views import view_cart
from cart import views as cart_views

urlpatterns = [
    path('',view_cart,name='view_cart'),
    path('cart/add/<int:product_id>', cart_views.add_cart, name='add_cart'),
    path('cart', cart_views.cart_detail, name='cart_detail'),
    ]