from django.db import models

# Create your models here.
class Transaction(models.Model):
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_date = models.DateField()
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', related_name='transactions', on_delete=models.CASCADE)

    def __str__(self):
        return self.description