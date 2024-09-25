from django.contrib import admin
from .models import Category, Product, Banner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_active']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active']
