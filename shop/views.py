from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Products, Category
# Create your views here.
 
def home(request, category_slug=None):
    category_page = None
    products = None
    if category_page!= None:
        category_page = get_object_or_404(Category,slug=category_slug)
        products = Products.objects.filter(category=category_page)
    else:
        products = Products.objects.all()
    return render(request, 'shop/index.html', {'category': category_page, 'products': products})
    

def index(request):
    product_objects = Products.objects.all()
 
    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
 
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request,'shop/index.html',{'product_objects':product_objects})
 
 
def detailPage(request,id):
    product_detail = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_detail':product_detail})