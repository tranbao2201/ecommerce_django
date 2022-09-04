from .models import Cart
from service.cart import CartService


def count_cart(request):
    if 'admin' in request.path:
        return {}
    else:
        cart_cou
        try:
            cart = Cart.objects.get(cart_id=CartService.get_cart_id(request))
            return {'cart': cart.get_total_item}
        except Cart.DoesNotExist:

