from django.shortcuts import render

# Create your views here.
def shop_view(request):
    pass

def cartPage(request):
    return render(request, 'cart.html')