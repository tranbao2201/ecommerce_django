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

    @classmethod
    def merge_cart(cls, request, user):
        try:
            session_cart = Cart.objects.get(
                cart_id=cls.get_cart_id(request))
            session_cart_items = session_cart.cart_items.all()
            if session_cart_items.exists():
                user_cart = user.cart
                if user_cart:
                    user_cart_items = user_cart.cart_items.all()
                    session_variation_ids = [list(cart_item.variations.values_list(
                        "id", flat=True)) for cart_item in session_cart_items]
                    user_variantion_ids = [list(cart_item.variations.values_list(
                        "id", flat=True)) for cart_item in user_cart_items]
                    for ids in session_variation_ids:
                        if ids in user_variantion_ids:
                            user_cart_item = user_cart_items[user_variantion_ids.index(
                                ids)]
                            session_cart_item = session_cart_items[session_variation_ids.index(
                                ids)]
                            user_cart_item.quantity += session_cart_item.quantity

                        else:
                            session_cart_item = session_cart_items[session_variation_ids.index(
                                ids)]
                            user_cart_item = user_cart.cart_items.add(
                                session_cart_item)
                        user_cart_item.save()
                else:
                    session_cart.user = user
                    session_cart.save()
        except:
            pass
