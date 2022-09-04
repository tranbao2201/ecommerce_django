from http.client import HTTPResponse
from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from store.models import Product
# Create your views here.


def cart(request):
    return render(request, 'store/cart.html', {})


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(cart_id=_cart_id(request))[0]
    cart_item = CartItem.objects.get_or_create(product=product, cart=cart)[0]
    cart_item.quantity = 1 is None ? cart_item.quantity = 1: cart_item.quantity += 1
    cart_item.save()
    return HTTPResponse(cart_item.quantity)
    return redirect('cart')


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
