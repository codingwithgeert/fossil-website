from django.test import TestCase
from django.urls import reverse, resolve
from .views import about_me, faq_page, contact

class TestUrls(TestCase):
        def test_about_url_is_checked(self):
            url = reverse('about')
            self.assertEqual(resolve(url).func, about_me)
            
        def test_faq_url_is_checked(self):
            url = reverse('faq')
            self.assertEqual(resolve(url).func, faq_page)
        
        def test_contact_url_is_checked(self):
            url = reverse('contact')
            self.assertEqual(resolve(url).func, contact)
    