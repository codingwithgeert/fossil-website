from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return '{}' .format(self.title)
        
class Products(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return '{}' .format(self.title)    
        
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_add = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'Cart'
        ordering = ['date_add']
        
    def __str__(self):
        return '{}' .format(self.cart_id)

class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
         db_table = 'CartItem'
    
    def sub_total(self):
        return self.product.price * self.quantity
        
    def __str__(self):
        return '{}' .format(self.product)