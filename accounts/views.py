from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from shop.models import Products, Category, Order, OrderItem
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import SignUpForm

# Create your views here.

def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            login(request, signup_user)
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
def logoutView(request):
    logout(request)
    return redirect('login')
    
@login_required(redirect_field_name='next', login_url='login')
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(email=email)
        print(request.user)
        
    return render(request, 'order_list.html', {'order_details': order_details})

@login_required(redirect_field_name='next', login_url='login')
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order = Order.objects.get(id=order_id, email=email)
        order_items = OrderItem.objects.filter(order=order)
    return render(request, 'view_order.html', {'order': order, 'order_items': order_items})