from django.shortcuts import render

def home(request):
    product = Product.objects.all().filter(is)
    return render(request,'home.html')