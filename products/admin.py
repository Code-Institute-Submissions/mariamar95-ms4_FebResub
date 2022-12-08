from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModeAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product)
admin.site.register(Category)
