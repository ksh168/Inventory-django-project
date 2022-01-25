from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)