from django.shortcuts import render

def home(request):
    product = Product.objects.all().filter(is_ava)
    return render(request,'home.html')