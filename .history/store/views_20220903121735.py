from turtle import end_fill
from django.shortcuts import render, get_object_or_404, get_list_or_404

from category.models import Category
from .models import Product
from category.models import Category
# Create your views here.


def store(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request):
    return render(request, 'store/product_detail.html', {'product
