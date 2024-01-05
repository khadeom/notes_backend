from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_signup(self):
        data = {'username': 'testuser', "email":"test@gmail.com", 'password': 'testpass'}
        response = self.client.post('/api/auth/signup/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login(self):
        # Create a user for testing
        User.objects.create_user(username='testuser', password='testpass')
        
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post('/api/auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
