from django.contrib import admin
from django.urls import path, include
from shop import views as shop_views
from django.conf.urls.static import static, serve
from .settings import MEDIA_ROOT
from django.conf import settings



urlpatterns = [
    path('',shop_views.index,name='index' ),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT }),
    path('<int:id>/',shop_views.detailPage,name='detail',),
  
]