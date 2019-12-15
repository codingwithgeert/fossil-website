from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.FloatField()
    category = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def __str__(self):
        return '{}' .format(self.title)