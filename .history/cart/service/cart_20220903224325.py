class CartService:
    @classmethod
    def get_cart_id(cls):
        cart = request.session.session_key
        if not cart:
            cart = request.session.create()
        return cart