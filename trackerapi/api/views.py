from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from datetime import datetime
#from django.contrib.auth.models import User

from .serializers import TransactionSerializer, UserSerializer
from .models import Transaction

# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
    # set default queryset
    queryset = Transaction.objects.all().order_by('id')
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Assign the current user as the user of the created transaction
        """
        serializer.save(user=self.request.user)

    # override default queryset to show only transactions of the current user
    def get_queryset(self):
        """
        This view should return a list of all the transactions
        for the currently authenticated user.
        """
        user = self.request.user
        # filter transactions of the current user
        # order by transaction_date, in descending order
        queryset = Transaction.objects.filter(user=user).order_by('-transaction_date')

        # filter by category and transaction date
        category = self.request.query_params.get('category')
        date_str = self.request.query_params.get('transaction_date')

        if category is not None:
            queryset = queryset.filter(category=category)

        if date_str is not None:
            # parse the string to a date object
            trans_date = datetime.strptime(date_str, '%Y-%m-%d')
            queryset = queryset.filter(transaction_date=trans_date)

        return queryset


# view for registering a new user
class RegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

# IF we want to expose users (with all methods available), uncomment this code block
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]