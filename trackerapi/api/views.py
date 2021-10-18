from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, generics
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
        return Transaction.objects.filter(user=user).order_by('id')

# view for registering a new user
class RegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

# IF we want to expose users (with all methods available), uncomment this code block
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]