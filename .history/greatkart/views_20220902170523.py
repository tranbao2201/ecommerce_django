from django.shortcuts import render


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        ''
    }
    return render(request, 'home.html')
