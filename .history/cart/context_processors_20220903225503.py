from .models import Cart
from service.cart import CartService


def count_cart(request):
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=CartService.get_cart_id(request))
            cart_count {'cart': cart.get_total_item}
        except Cart.DoesNotExist:
            
