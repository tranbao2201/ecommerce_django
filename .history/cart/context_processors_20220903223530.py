from .models import Cart


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
