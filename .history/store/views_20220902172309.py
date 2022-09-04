from django.shortcuts import render

# Create your views here.

def store(request, *args, **kwargs):
    return render(request, 'soterstore.html', kwargs)
