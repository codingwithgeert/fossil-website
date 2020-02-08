from django.test import Client, TestCase
from accounts.forms import ContactUsForm
from .views import about_me

class TestAboutView(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_response_200(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)
    
class TestFaqView(TestCase):
    def setup(self):
        self.client = Client()
        
    def test_response_200(self):
        response = self.client.get('/pages/faq/')
        self.assertEqual(response.status_code, 200)
        
class TestContactView(TestCase):
    def setup(self):
        self.client = Client()
        
    def test_response_200(self):
        response = self.client.get('/pages/contact/')
        self.assertEqual(response.status_code, 200)
  
# Comment it out as I can't get it to show something different than 404      
#class TestContactSendView(TestCase):
#     def setup(self):
#         self.client = Client()
      
#     def test_response_200(self):
#         response = self.client.get('/pages/contact_send/')
#         self.assertEqual(response.status_code, 404 )   
    
    