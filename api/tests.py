from django.test import TestCase
from django.test.client import Client

class ApiTestClass(TestCase):
    
    fixtures = ['test_data.json',]
    
    def setUp(self):
        pass

    def testurl1(self):
        c = Client()
        response = c.get('/api/page/2')
        return response.status_code
    
    def testurl2(self):
        c = Client()
        response = c.get('/api/pages/0/10')
        return response.status_code