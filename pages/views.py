from django.shortcuts import render
from shop.models import Products
from pages.views import detail_page

# Create your views here.
def detail_page(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'pages/details.html',{'product_object':product_object})