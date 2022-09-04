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
        for cart_item in self.cart_items:
            total_item =


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.product
