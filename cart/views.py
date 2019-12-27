from django.shortcuts import render, redirect
from shop.models import Products, Cart, CartItem

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart/cart.html")
    
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


