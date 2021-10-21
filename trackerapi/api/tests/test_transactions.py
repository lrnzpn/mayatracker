from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from api.models import Transaction

class TestTransactions(APITestCase):

    def setUp(self):
        # Test data
        self.user = {
            'username': 'sample',
            'email': 'sample@example.com',
            'password': 'password123'
        }
        self.transaction = {
            'description': 'GigaSurf',
            'category': 'Load',
            'amount': 99,
            'transaction_date':'2020-10-20'
        }
        self.new_user = {
            'username': 'sample2',
            'email': 'sample2@example.com',
            'password': 'password123'
        }
        self.new_transaction = {
            'description': 'GigaVideo',
            'category': 'Internet',
            'amount': 399,
            'transaction_date':'2020-10-21'            
        }
        # Create a user
        self.create_user(self.user['username'], self.user['email'], self.user['password'])
        # Create a transaction
        self.transaction_response = self.client.post('/api/v1/transactions/', self.transaction, format='json')
        
         # Test data for 404 errors
        self.new_url = self.transaction_response.data['url'][:-2]
        self.new_url = self.new_url + '5/'
        self.invalid_access_token = '12345'

    def create_user(self, username, email, password):
        User.objects.create_user(username=username, email=email, password=password)
        new_login_response = self.client.post('/api/v1/login/', {'username':username, 'password':password},format='json')
        new_access_token = new_login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + new_access_token)
        
    # CREATE TRANSACTION
    def test_create_transaction_success(self):
        self.assertEqual(self.transaction_response.status_code, 201)
        self.assertEqual(Transaction.objects.get().description, self.transaction['description'])
        self.assertEqual(Transaction.objects.get().category, self.transaction['category'])
        self.assertEqual(Transaction.objects.get().amount, self.transaction['amount'])
        self.assertEqual(Transaction.objects.get().transaction_date.strftime('%Y-%m-%d'), self.transaction['transaction_date'])

    def test_create_transaction_error_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.invalid_access_token)
        response = self.client.put('/api/v1/transactions/', self.transaction, format='json')
        self.assertEqual(response.status_code, 401)

    # READ TRANSACTION
    def test_read_transaction_success(self):
        response = self.client.get(self.transaction_response.data['url'])
        self.assertIn('url', response.data)
        self.assertIn('description', response.data)
        self.assertIn('category', response.data)
        self.assertIn('amount', response.data)
        self.assertIn('transaction_date', response.data)
        self.assertIn('created_at', response.data)
        self.assertIn('updated_at', response.data)
        self.assertEqual(response.status_code, 200)

    def test_read_transactions_list_success(self):
        response = self.client.get('/api/v1/transactions/')
        self.assertEqual(response.status_code, 200)

    def test_read_transactions_list_filter_category_success(self):
        response = self.client.get('/api/v1/transactions/', {'category': 'Load'})
        self.assertEqual(response.status_code, 200)

    def test_read_transactions_list_filter_txn_date_success(self):
        response = self.client.get('/api/v1/transactions/', {'transaction_date': '2020-10-20'})
        self.assertEqual(response.status_code, 200)

    def test_read_transaction_error_data_not_found(self):
        response = self.client.get(self.new_url)
        self.assertEqual(response.status_code, 404)

    def test_read_transaction_error_user_not_owner(self):
        self.create_user(self.new_user['username'], self.new_user['email'], self.new_user['password'])
        response = self.client.get(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 404)

    def test_read_transaction_error_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.invalid_access_token)
        response = self.client.get(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 401)

    def test_read_transactions_list_error_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.invalid_access_token)
        response = self.client.delete(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 401)

    # UPDATE TRANSACTION
    def test_update_transaction_success(self):
        response = self.client.put(self.transaction_response.data['url'], self.new_transaction, format='json')
        self.assertEqual(Transaction.objects.get().description, self.new_transaction['description'])
        self.assertEqual(Transaction.objects.get().category, self.new_transaction['category'])
        self.assertEqual(Transaction.objects.get().amount, self.new_transaction['amount'])
        self.assertEqual(Transaction.objects.get().transaction_date.strftime('%Y-%m-%d'), self.new_transaction['transaction_date'])
        self.assertEqual(response.status_code, 200)
    
    def test_update_transaction_error_data_not_found(self):
        response = self.client.put(self.new_url, self.new_transaction, format='json')
        self.assertEqual(response.status_code, 404)

    def test_update_transaction_error_user_not_owner(self):
        self.create_user(self.new_user['username'], self.new_user['email'], self.new_user['password'])
        response = self.client.put(self.transaction_response.data['url'], self.new_transaction, format='json')
        self.assertEqual(response.status_code, 404)

    def test_update_transaction_error_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.invalid_access_token)
        response = self.client.put(self.transaction_response.data['url'], self.new_transaction, format='json')
        self.assertEqual(response.status_code, 401)

    # DELETE TRANSACTION
    def test_delete_transaction_success(self):
        response = self.client.delete(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 204)

    def test_delete_transaction_error_data_not_found(self):
        response = self.client.delete(self.new_url)
        self.assertEqual(response.status_code, 404)

    def test_delete_transaction_error_user_not_owner(self):
        self.create_user(self.new_user['username'], self.new_user['email'], self.new_user['password'])
        response = self.client.delete(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 404)

    def test_delete_transaction_error_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.invalid_access_token)
        response = self.client.delete(self.transaction_response.data['url'])
        self.assertEqual(response.status_code, 401)

    # TEST TRANSACTION MODEL
    def test_transaction_model(self):
        user = User.objects.create_user(username=self.new_user['username'], password=self.new_user['password'])
        transaction= Transaction.objects.create(description='GigaSurf', category='Load', amount=99, transaction_date='2020-10-20', user=user)
        self.assertTrue(isinstance(transaction, Transaction))
        self.assertEqual(str(transaction), 'GigaSurf')