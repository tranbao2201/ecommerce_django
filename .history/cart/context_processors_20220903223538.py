from .models import Cart


def count(request):
    links = Category.objects.all()
    return dict(links=links)
