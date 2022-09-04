from django.shortcuts import render
from cart.models import Cart
from store.models import Product
# Create your views here.


def cart(request):
    return render(request, 'store/cart.html', {})


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get_or_create(product=product, cart=cart)
    cart_item.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
