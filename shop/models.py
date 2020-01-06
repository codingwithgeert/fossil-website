from django.db import models

# Create your models here.
# Category model:
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
#Product Model:        
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
        
#Cart Model:        
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_add = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'Cart'
        ordering = ['date_add']
        
    def __str__(self):
        return '{}' .format(self.cart_id)
        
#CartItem Model:
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
        
class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='EUR Order Total')
    email = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    #Billing Model
    billing_name = models.CharField(max_length=250, blank=True)
    billing_address1 = models.CharField(max_length=250, blank=True)
    billing_city = models.CharField(max_length=250, blank=True)
    billing_postcode = models.CharField(max_length=250, blank=True)
    billing_country = models.CharField(max_length=250, blank=True)
    #Shipping Model
    shipping_name = models.CharField(max_length=250, blank=True)
    shipping_address1 = models.CharField(max_length=250, blank=True)
    shipping_city = models.CharField(max_length=250, blank=True)
    shipping_postcode = models.CharField(max_length=250, blank=True)
    shipping_country = models.CharField(max_length=250, blank=True)
    
    class Meta:
        db_table = 'Order'
        ordering = ['-created']
        
    def __str__(self):
        return '{}' .format(self.id)
        
class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='EUR Price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'OrderItem'
    
    def sub_total(self):
        return self.quantity * self.price
        
    def __str__(self):
        return '{}' .format(self.product)