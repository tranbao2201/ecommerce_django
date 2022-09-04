from turtle import end_fill
from django.shortcuts import render, get_object_or_404, get_list_or_404

from category.models import Category
from .models import Product
from category.models import Category
from django.core.paginator import Paginator
# Create your views here.


def store(request, category_id=None):
    search_keyword = request.GET.get('search_keyword')
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    if search_keyword:
        products = products.filter(name__icontains=search_keyword)
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 6)
    products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_id=None, product_id=None):
    product = get_object_or_404(
        Product, id=product_id, category_id=category_id)
    context = {'product': product, }
    return render(request, 'store/product_detail.html', context)
