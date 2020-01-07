from django.contrib import admin
from .models import Category, Products, OrderItem, Order

# Register your models here.

admin.site.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price']
    list_editable = ['price', 'discount_price']
    list_per_page = 7

admin.site.register(Products, ProductAdmin)

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Products', {'fields': ['product'], }),
        ('Quantity', {'fields': ['quantity'], }),
        ('Price', {'fields': ['price'], }),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    # For testing purpose its off now
    #can_delete = False
    max_num = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billing_name', 'email', 'created']
    list_display_links = ('id', 'billing_name')
    search_fields = ['id', 'billing_nameName', 'email']
    readonly_fields = ['id', 'token', 'total', 'email', 'created',
                       'billing_name', 'billing_address1', 'billing_city', 'billing_postcode',
                       'billing_country', 'shipping_name', 'shipping_address1', 'shipping_city',
                       'shipping_postcode', 'shipping_country']

    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
        ('BILLING INFORMATION', {'fields': ['billing_name', 'billing_address1',
                                            'billing_city', 'billing_postcode', 'billing_country', 'email']}),
        ('SHIPPING INFORMATION', {'fields': ['shipping_name', 'shipping_address1',
                                             'shipping_city', 'shipping_postcode', 'shipping_country']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]
    # For testing purpose its off now
    #def has_delete_permission(self, request, obj=None):
        #return False

    #def has_add_permission(self, request):
        #return False