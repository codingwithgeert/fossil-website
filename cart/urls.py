from django.urls import path
from cart import views as cart_views

urlpatterns = [
    path('cart',cart_views.cartPage,name='cart' ),
    ]