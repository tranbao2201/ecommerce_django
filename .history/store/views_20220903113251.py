from django.shortcuts import render
from .models import Product
# Create your views here.


def store(request, *args, **kwargs):
    products = Product.objects.all().filter(is_available=True)
    product = products.count()
    context = {
        'products': products,
        'product': product,
    }
    return render(request, 'store/store.html', context)
