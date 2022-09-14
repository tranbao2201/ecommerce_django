from django.db import models
from accounts.models import Account
from store.models import Product, VariationProduct

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True,
                                related_name='cart')
    cart_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

    def get_total_item(self):
        return sum(map(lambda x: x.quantity, self.cart_items.all()))

    def get_total_price(self):
        return sum(map(lambda x: x.quantity * x.product.price, self.cart_items.all()))


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(
        VariationProduct, related_name="variations")
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField(default=0)
    is_activate = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity
