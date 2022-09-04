from django.shortcuts import render
from .models import Product
# Create your views here.


def store(request, *args, **kwargs):
    products = Product.objects.all().filter(is_available=True)
    print(products)
    context = {
        'products': products,
    }
    return render(request, 'store/store.html', context)
