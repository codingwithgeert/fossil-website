from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    product_item = Product.object.all()
    return render(request, 'shop/index.html', {'product_item':product_item})
    