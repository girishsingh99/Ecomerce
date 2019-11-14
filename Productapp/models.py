from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length =100)
    price = models.FloatField()
    catagory = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    qty= models.IntegerField()
