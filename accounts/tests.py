import json
from django.http import response
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User

class PublicAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            unit = '0000',
            password = '1234',
            is_superuser = 1
        ),
        
        self.user = User.objects.create(
            unit = '1001',
            password = '1234',
            cost = '1000'
        )
        
    def test_Public_post_success(self):
        data = {'unit' : '1001', 'password':'1234'}
        self.client.credentials(HTTP_AUTHORIZATION='10011234')
        response = self.client.post(
            '/api/accounts/public',
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'public' : {'unit':'1001', 'cost':'1000'}})