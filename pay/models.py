from django.db import models

# Create your models here.
from django.db import models
class Transaction(models.Model):
    amount = models.IntegerField(default=0)
    description = models.TextField(verbose_name='description')
    salt = models.CharField(max_length=25, verbose_name='salt')

