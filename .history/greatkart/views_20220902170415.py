from django.shortcuts import render

def home(request):
    product = Prod
    return render(request,'home.html')