
def menu_links(request):
    links = Category.objects.all()
    return dict()