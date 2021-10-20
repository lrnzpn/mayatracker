from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from faker import Faker

class TestUsers(APITestCase):

    def setUp(self):
        # Generate user data
        self.fake = Faker()
        self.user = {
            'username': self.fake.email().split('@')[0],
            'email': self.fake.email(),
            'password': self.fake.email()
        }
        # Create a user
        self.user_response = self.client.post('/api/v1/register/', self.user, format="json")
        
    def test_can_register(self):
        self.assertEqual(self.user_response.status_code, 201)
        self.assertEqual(User.objects.get().email, self.user['email'])
        self.assertEqual(User.objects.get().username, self.user['username'])

    def test_can_login(self):
        response = self.client.post('/api/v1/login/', {'username': self.user['username'], 'password': self.user['password']}, format="json")
        self.assertEqual(response.status_code, 200)

    def test_cannot_register_user_already_exist(self):
        response = self.client.post('/api/v1/register/', self.user, format="json")
        self.assertEqual(response.status_code, 400)

    def test_cannot_login_wrong_creds(self):
        data = {
            'username': self.user['username'],
            'password': self.user['password'] + 'a'
        }
        response = self.client.post('/api/v1/login/', data, format="json")
        self.assertEqual(response.status_code, 401)