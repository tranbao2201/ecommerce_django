from django.shortcuts import render

def home(request):
    product = Product.objects.all().filter
    return render(request,'home.html')