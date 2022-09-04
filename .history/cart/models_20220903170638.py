from re import T
from django.db import models
from functools import reduce
from store.models import Product

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

    def get_total_items(self):
        return sum(map(lambda x: x.quantity, list(self.cart_items.all())))


class CartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    cart=models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    quantity=models.IntegerField(default=0)
    is_activate=models.BooleanField(default=True)
