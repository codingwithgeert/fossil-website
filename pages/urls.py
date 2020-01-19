from django.urls import path
from pages import views as pages_views

urlpatterns = [
    path('pages/about/', pages_views.about_me, name='about'),
    path('pages/faq/', pages_views.faq_page, name='faq'),
    ]