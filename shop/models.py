from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images')