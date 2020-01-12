from django.shortcuts import render, redirect, reverse, get_object_or_404
from shop.models import Products, Cart, CartItem, Order, OrderItem 
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings

# Create your views here.

def view_cart(request):
    """
    A View that renders the cart contents page
    """
    return render(request, "cart.html")
    
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    """
    Add items to your cart
    """
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()

    return redirect('cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    """
    Show a page with the cart details
    """
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'the-fossil-shop - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billing_name = request.POST['stripeBillingName']
            billing_address1 = request.POST['stripeBillingAddressLine1']
            billing_city = request.POST['stripeBillingAddressCity']
            billing_postcode = request.POST['stripeBillingAddressZip']
            billing_country = request.POST['stripeBillingAddressCountryCode']
            shipping_name = request.POST['stripeShippingName']
            shipping_address1 = request.POST['stripeShippingAddressLine1']
            shipping_city = request.POST['stripeShippingAddressCity']
            shipping_postcode = request.POST['stripeShippingAddressZip']
            shipping_country = request.POST['stripeShippingAddressCountryCode']
            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency='eur',
                description=description,
                customer=customer.id
            )
            """
            Saves the Order
            """
            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    email=email,
                    billing_name=billing_name,
                    billing_address1= billing_address1,
                    billing_city=billing_city,
                    billing_postcode=billing_postcode,
                    billing_country=billing_country,
                    shipping_name=shipping_name,
                    shipping_address1=shipping_address1,
                    shipping_city=shipping_city,
                    shipping_postcode=shipping_postcode,
                    shipping_country=shipping_country
                )
                order_details.save()
                for order_item in cart_items:
                    or_item = OrderItem.objects.create(
                        product=order_item.product.title,
                        quantity=order_item.quantity,
                        price=order_item.product.price,
                        order=order_details
                    )
                    or_item.save()

                    # print a message when the order is created
                    print('the order has been created')
                return redirect('thank_you', order_details.id)
            except ObjectDoesNotExist:
                    pass
                    
                
        except stripe.error.CardError as e:
            return False, e

    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter, data_key=data_key, stripe_total=stripe_total, description=description))

def cart_remove(request, product_id):
    """
    Minus item from the cart
    """
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def trashbin_product(request, product_id):
    """
    Delete item from the cart
    """
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')
    

def thank_you(request, order_id):
    """
    Shows a page when the order was succesfull
    """
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
    return render(request, 'ordsuccess.html', {'customer_order': customer_order})