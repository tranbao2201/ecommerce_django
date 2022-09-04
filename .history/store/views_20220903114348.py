from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def store(request, category_id=None):
    if category_id:
        product = get_list(Product, id=category_id)
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
