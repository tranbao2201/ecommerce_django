from .models import Cart


def count_cart(request):
    links = Category.objects.all()
    return dict(links=links)
