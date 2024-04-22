from django.contrib import admin

from catalog.models import Product, Category, Version


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_for_purchase', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Version)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'current_version')
