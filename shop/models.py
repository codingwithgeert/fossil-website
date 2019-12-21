from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    
    def __str__(self):
        return '{}' .format(self.title)
        
    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Products(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    
    
    def __str__(self):
        return '{}' .format(self.title)    
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    