from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('<int:product_>', views.add_cart, name='add_cart'),
]
