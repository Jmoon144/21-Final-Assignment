import json

from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api.publics.models import Public
    
class AdminAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='root2',
            password='go9511455',
            is_staff = True
        )
        
        self.token = Token.objects.create(user=self.user)
        Public.objects.create(id=1, password=1234, number='2001', cost='1000')
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_Public_list_post_success(self):
        response = self.client.get('/api/admin')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{'number':'2001', 'cost':'1000', 'password':'1234'}])
    
    def test_Public_list_user_none(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/admin')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)