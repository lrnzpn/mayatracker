from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from api.models import Transaction
from faker import Faker
from datetime import datetime
import requests

class TestTransactions(APITestCase):

    def setUp(self):
        # Generate user data
        self.fake = Faker()
        self.user = {
            'username': self.fake.email().split('@')[0],
            'email': self.fake.email(),
            'password': self.fake.email()
        }
        # Generate transaction data
        self.transaction = {
            'description': 'food',
            'category': 'food',
            'amount': self.fake.pydecimal(left_digits=3, right_digits=2),
            'transaction_date': datetime.today().strftime('%Y-%m-%d')
        }
        # Create a user
        User.objects.create_user(username=self.user['username'], password=self.user['password'])
        # Login
        login_response = self.client.post('/api/v1/login/', {'username':self.user['username'], 'password':self.user['password']},format='json')
        # Get user access token
        access_token = login_response.data['access']
        # Set authorization header
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + access_token)
        # Create a transaction
        self.transaction_response = self.client.post('/api/v1/transactions/', self.transaction, format='json')

    def test_can_create_transaction(self):
        self.assertEqual(self.transaction_response.status_code, 201)

    def test_can_get_transaction(self):
        response = self.client.get(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 200)

    def test_can_update_transaction(self):
        response = self.client.put(self.transaction_response.data['url'], self.transaction, format='json')
        self.assertEqual(response.status_code, 200)

    def test_can_delete_transaction(self):
        response = self.client.delete(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 204)

    def test_can_list_transactions(self):
        response = self.client.get(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 200)