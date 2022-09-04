from django.shortcuts import render

def home(request):
    product = Product.obje
    return render(request,'home.html')