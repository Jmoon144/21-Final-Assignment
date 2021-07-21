import json

from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api.publics.models import Public

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data  = {
            'username'  : 'root',
            'email'     : 'sjwm98@naver.com',
            'password1' : 'go9511455',
            'password2' : 'go9511455',
        }                                                                                                                                                                                                                                                                                                                                                                                                      
        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
class PublicAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='root',
            password='go9511455',
            is_staff = True
        )
        
        self.token = Token.objects.create(user=self.user)
        Public.objects.create(id=1, password=1234, number='2001', cost='1000')
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_Public_authenticated(self):
        data = {'number':'2001', 'password':'1234'}

        response = self.client.post('/api/public', data =json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'public' : {'number':'2001', 'password':'1234', 'cost':'1000'}})

    def test_Public_list_user_none(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/public')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)