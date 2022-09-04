from django.shortcuts import render


def home(request):
    product = Product.objects.all().filter(is_available=True)
    return render(request, 'home.html')
