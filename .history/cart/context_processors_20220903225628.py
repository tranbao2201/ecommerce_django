from .models import Cart
from service.cart import CartService


def count_cart(request):
    if 'admin' in request.path:
        return {}
    else:
        cart_count = {'cart_count': 0}
        try:
            cart = Cart.objects.get(cart_id=CartService.get_cart_id(request))
            cart_count.update(cart_count=cart.get_total_item())
        except Cart.DoesNotExist:
            pass
        return cart_count
