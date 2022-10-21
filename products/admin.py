from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = (
                   'product_name',
                   'price',
                   'old_price',
                   'stock',
                   'category',
                   'is_available')


admin.site.register(Product, ProductAdmin)
