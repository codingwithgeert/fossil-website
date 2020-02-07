from django.test import TestCase
from django.urls import reverse, resolve
from .views import add_cart

class TestUrls(TestCase):
    
        def test_add_url_is_checked(self):
            url = reverse('add_cart')
            self.assertEqual(resolve(url).func, add_cart)
            
        def test_add_url_is_resolved(self):
            url = reverse('add_cart', args=['product-id'])
            self.assertEqual(resolve(url).func, add_cart)    
            
       