from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('', views.add_cart, name='add_cart'),
]