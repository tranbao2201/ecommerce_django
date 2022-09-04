from django.shortcuts import render

def home(request):
    product = Product.o
    return render(request,'home.html')