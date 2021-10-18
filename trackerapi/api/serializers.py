from rest_framework import serializers

from .models import Transaction
from django.contrib.auth.models import User

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Transaction
        fields = ('id', 'description', 'amount', 'transaction_date', 'created_at', 'updated_at', 'user')
        read_only_fields = ['created_at', 'updated_at', 'user']

class UserSerializer(serializers.ModelSerializer):
    # add the transactions object as part of the user containing the primary keys of the transactions related to the user
    transactions = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'transactions']