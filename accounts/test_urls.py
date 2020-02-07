from django.test import TestCase
from django.urls import reverse, resolve
from .views import signupView, loginView, logoutView, orderHistory

class TestUrls(TestCase):
        def test_signup_url_is_checked(self):
            url = reverse('signup')
            self.assertEqual(resolve(url).func, signupView)
            
        def test_login_url_is_checked(self):
            url = reverse('login')
            self.assertEqual(resolve(url).func, loginView)
        
        def test_logout_url_is_checked(self):
            url = reverse('logout')
            self.assertEqual(resolve(url).func, logoutView)
        
        def test_order_history_is_checked(self):
            url = reverse('order_history')
            self.assertEquals(resolve(url).func, orderHistory)
        
            

