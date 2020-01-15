from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('account/create/', accounts_views.signupView, name='signup'),
    path('account/login/', accounts_views.loginView, name='login'),
    path('account/logout', accounts_views.logoutView, name='logout'),
    path('order_history/', accounts_views.orderHistory, name='order_history'),
    ]