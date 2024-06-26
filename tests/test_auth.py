from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        }

    def test_user_registration(self):
        response = self.client.post(reverse('user-list'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username=self.user_data['username']).exists())

    def test_user_login(self):
        # Register the user first
        self.client.post(reverse('user-list'), self.user_data)
        response = self.client.post(reverse('login'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.data)

        self.auth_token = response.data['auth_token']

    def test_access_protected_endpoint(self):
        # Register the user first
        self.client.post(reverse('user-list'), self.user_data)
        # Login the user to get the token
        response = self.client.post(reverse('login'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.auth_token = response.data['auth_token']

        # Use the token to access a protected endpoint
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.auth_token)
        response = self.client.get(reverse('bookings'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
