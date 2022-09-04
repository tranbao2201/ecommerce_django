from django.shortcuts import render
from store.models import Product
# Create your views here.


def cart(request):
    return render(request, 'store/cart.html', {})


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(cart_id=cart_id(request))

def _cart_id(request):
    cart = 