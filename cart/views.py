from statistics import variance
from django.shortcuts import get_object_or_404, render, redirect
from cart.models import Cart, CartItem
from cart.service.cart import CartService
from store.managers.variation_product import VariationProductQuerySet
from store.models import Product, VariationProduct, VariationType
from django.db.models import Q
# Create your views here.


def cart(request):
    try:
        cart = Cart.objects.get(cart_id=CartService.get_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        total_item = cart.get_total_item()
        total_price = cart.get_total_price()
    except Cart.DoesNotExist:
        cart_items = []
        total_item = 0
        total_price = 0
    context = {
        'cart_items': cart_items,
        'total_item': total_item,
        'total_price': total_price,
    }

    return render(request, 'store/cart.html', context)


def add_cart(request, product_id):
    data = request.POST.copy()
    color = data.get('color')
    size = data.get('size')
    product = Product.objects.get(id=product_id)
    _filter = Q(variation_type=VariationType.COLOR, variation_value=color) | Q(
        variation_type=VariationType.SIZE, variation_value=size)
    variations = VariationProduct.objects.filter(_filter, product=product)
    cart = Cart.objects.get_or_create(
        cart_id=CartService.get_cart_id(request))[0]
    cart_items = CartItem.objects.filter(
        product=product, cart=cart, variations=variations.first())
    item = CartItem.objects.none()
    for cart_item in cart_items:
        if set(cart_item.variations.all()) == set(variations):
            item = cart_item
            break
    if not item:
        item = CartItem.objects.create(product=product, cart=cart)
        item.variations.add(*variations)
    item.quantity += 1
    item.save()
    _update_product_stock(product, -1)
    return redirect('cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=CartService.get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except cart_item.DoesNotExist:
        pass
    _update_product_stock(product, 1)
    return redirect('cart')


def remove_cart_item(request, cart_id):
    try:
        cart_item = CartItem.objects.get(id=cart_id)
        cart_item.delete()
        _update_product_stock(cart_item.product, cart_item.quantity)
    except cart_item.DoesNotExist:
        pass
    return redirect('cart')


def _update_product_stock(product: Product, quantity: int) -> Product:
    product.stock += quantity
    product.save()
    return product
