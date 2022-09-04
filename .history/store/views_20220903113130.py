from django.shortcuts import render
from .models import Product
# Create your views here.


def store(request, *args, **kwargs):
    products = Product.objects.all().filter(is_available=True)
    proudct_count = products.count()
    context = {
        'products': products,
        'proudct_count': proudct_count,
    }
    return render(request, 'store/store.html', context)
