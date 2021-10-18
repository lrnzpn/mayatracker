from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TransactionSerializer
from .models import Transaction

# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('id')
    serializer_class = TransactionSerializer