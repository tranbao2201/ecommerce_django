from cart.models import Cart


class CartService:
    @classmethod
    def get_cart_id(cls, request):
        cart = request.session.session_key
        if not cart:
            cart = request.session.create()
        return cart

    @classmethod
    def get_cart(cls, request):
        try:
            if request.user.is_authenticated:
                cart = Cart.objects.get(user=request.user)
            else:
                cart = Cart.objects.get(cart_id=cls.get_cart_id(request))
        except Cart.DoesNotExist:
            cart = None
        return cart

    @classmethod
    def create_cart(cls, request):
        return Cart.objects.create(user_id=request.user.id,
                                   cart_id=cls.get_cart_id(request))