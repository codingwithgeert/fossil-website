from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('account/create/', accounts_views.signupView, name='signup'),
    ]

