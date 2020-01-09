from django.shortcuts import render
from django.contrib.auth.models import Group, User
from .forms import RegisterForm
# Create your views here.

def signupView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
    