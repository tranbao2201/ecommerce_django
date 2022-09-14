from .models import Cart
from .service.cart import CartService


def count_cart(request):
    if 'admin' in request.path:
        return {}
    else:
        cart_count = 0
        cart = CartService.get_cart(request)
        cart_count = 0 if cart is None else cart.get_total_item()
        return dict(cart_count=cart_count)
