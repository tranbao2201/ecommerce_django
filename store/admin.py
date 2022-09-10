from django.contrib import admin
from .models import Product, VariationProduct

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price',
                    'stock', 'updated_at', 'is_available')


class VariationProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_type',
                    'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_type', 'variation_value', 'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(VariationProduct, VariationProductAdmin)
