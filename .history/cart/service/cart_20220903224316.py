class CartService:
    @classmethod
    def get_cart_id(cls):
        def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart