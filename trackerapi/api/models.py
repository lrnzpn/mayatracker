from django.db import models

# Create your models here.
class Transaction(models.Model):
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    transactionDate = models.DateField()

    def __str__(self):
        return self.description