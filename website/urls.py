"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop import views as shop_views
from cart import views as cart_views
from cart import urls as urls_cart
from accounts import views as accounts_views
from django.conf.urls.static import static, serve
from .settings import MEDIA_ROOT
from django.conf import settings



urlpatterns = [
    #/admin
    path('admin/', admin.site.urls),
    path('',shop_views.index,name='index' ),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT }),
    path('category/<slug:category_slug>', shop_views.home, name='products_by_category'),
    path('<int:id>/',shop_views.detailPage,name='detail',),
    path('cart/', include(urls_cart)),
    path('account/create/', accounts_views.signupView, name='signup'),
    path('account/login/', accounts_views.loginView, name='login'),
    path('account/logout', accounts_views.logoutView, name='logout'),
    path('order_history/', accounts_views.orderHistory, name='order_history'),
    path('order/<int:order_id>', accounts_views.viewOrder, name='order_detail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)