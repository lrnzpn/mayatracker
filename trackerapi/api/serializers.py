from rest_framework import serializers

from .models import Transaction
from django.contrib.auth.models import User

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    #user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Transaction
        fields = ('url', 'description', 'amount', 'transaction_date', 'category', 'created_at', 'updated_at')
        read_only_fields = ['created_at', 'updated_at']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # do not return the password field in the response
    password = serializers.CharField(write_only=True)

    # override the default create method
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']