from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'stock', 'updated_at', 'is_available', ')