from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, render, redirect
from cart.models import Cart, CartItem
from store.models import Product
# Create your views here.


def cart(request):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        total_item = cart.get_total_item()
        total_price = cart.get_total_price()
    except:
        pass
    context = {
        'cart_items': cart_items,
        'total_item': total_item,
        'total_price': total_price,
    }

    return render(request, 'store/cart.html', context)


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(cart_id=_cart_id(request))[0]
    cart_item = CartItem.objects.get_or_create(product=product, cart=cart)[0]
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def remove_cart(self, product_id):
    cart = Cart.objects.get(cart_id=_cart_id)
    product = get_object_or_404(id=product_id)
    


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
