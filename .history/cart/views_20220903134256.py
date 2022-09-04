from django.shortcuts import render

# Create your views here.

def cart(request):
    cart = cart_view(request)
    return render(request, 'cart.html', {'cart': cart})
