from .models import Cart
from service.cart import CartService

def count_cart(request):
    if 'admin' in request.path:
        return {}
    else:
        cart
