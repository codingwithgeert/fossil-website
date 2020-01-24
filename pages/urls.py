from django.urls import path
from pages import views as pages_views

urlpatterns = [
    path('about/', pages_views.about_me, name='about'),
    path('faq/', pages_views.faq_page, name='faq'),
    ]