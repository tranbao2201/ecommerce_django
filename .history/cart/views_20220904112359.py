from django.core
from django.shortcuts import get_object_or_404, render, redirect
from cart.models import Cart, CartItem
from cart.service.cart import CartService
from store.models import Product
# Create your views here.


def cart(request):
    try:
        cart = Cart.objects.get(cart_id=CartService.get_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        total_item = cart.get_total_item()
        total_price = cart.get_total_price()
    except Cart.DoesNotExist:
        pass
    context = {
        'cart_items': cart_items,
        'total_item': total_item,
        'total_price': total_price,
    }

    return render(request, 'store/cart.html', context)


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(cart_id=CartService.get_cart_id(request))[0]
    cart_item = CartItem.objects.get_or_create(product=product, cart=cart)[0]
    cart_item.quantity += 1
    cart_item.save()
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
