class CartService:
    @classmethod
    def get_cart_id(cls, request):
        cart = request.session.session_key
        if not cart:
            cart = request.session.create()
        return cart