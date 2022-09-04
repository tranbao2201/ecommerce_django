from .models import Cart


def count_cart(request):
    if 'admin' in request.path:
        return count
