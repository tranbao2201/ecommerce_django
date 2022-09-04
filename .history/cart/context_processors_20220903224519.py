from .models import Cart
from 

def count_cart(request):
    if 'admin' in request.path:
        return {}
    else:
        cart
