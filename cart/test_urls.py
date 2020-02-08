from django.test import TestCase
from django.urls import path, reverse, resolve
from .views import cart_detail, thank_you
from shop.models import Products, Order

class TestUrls(TestCase):
        def test_cart_detail_url_is_checked(self):
            url = reverse('cart_detail')
            self.assertEqual(resolve(url).func, cart_detail)