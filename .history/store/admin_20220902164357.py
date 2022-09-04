from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'slug', 'price', 'image', 'created_at')