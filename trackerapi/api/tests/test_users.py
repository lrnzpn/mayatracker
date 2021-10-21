from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class TestUsers(APITestCase):

    def setUp(self):
        # Test data
        self.user = {
            'username': 'sample',
            'email': 'sample@example.com',
            'password': 'password123'
        }
        # Create a user
        self.user_response = self.client.post('/api/v1/register/', self.user, format="json")
    
    # REGISTER
    def test_register_success(self):
        self.assertEqual(self.user_response.status_code, 201)
        self.assertEqual(User.objects.get().email, self.user['email'])
        self.assertEqual(User.objects.get().username, self.user['username'])

    def test_register_error_user_already_exists(self):
        response = self.client.post('/api/v1/register/', self.user, format="json")
        self.assertEqual(response.status_code, 400)
    
    # LOGIN
    def test_login_success(self):
        response = self.client.post('/api/v1/login/', {'username': self.user['username'], 'password': self.user['password']}, format="json")
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.status_code, 200)

    def test_login_error_wrong_username(self):
        self.user['username'] = 'sampleeee'
        response = self.client.post('/api/v1/login/', self.user, format="json")
        self.assertEqual(response.status_code, 401)

    def test_login_error_wrong_password(self):
        self.user['password'] = 'password'
        response = self.client.post('/api/v1/login/', self.user, format="json")
        self.assertEqual(response.status_code, 401)