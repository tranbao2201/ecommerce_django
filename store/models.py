from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to="photos/products")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args=[self.category.id, self.id])

    def is_out_of_stock(self):
        return self.stock <= 0


class VariationType:
    SIZE = 0
    COLOR = 1
    VARIANT_CHOICES = (
        (SIZE, 'size'),
        (COLOR, 'color'),
    )


class VariationProduct(models.Model):
    from store.managers.variation_product import VariationProductManager

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='variations')
    variation_type = models.IntegerField(
        default=0, choices=VariationType.VARIANT_CHOICES)
    variation_value = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = VariationProductManager()

    def __str__(self):
        return self.variation_value
