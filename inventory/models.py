from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    date_posted = models.DateTimeField(default=timezone.now)


    #dunder str method
    #used when Product.objects.first() is written in shell [python manage.py shell]
    def __str__(self):
        return self.product_name