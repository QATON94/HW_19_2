from django.contrib import admin

from catalog.models import Product, Category, Blog


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_for_purchase', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'contents', 'created_at', 'publication_sign')
    list_filter = ('publication_sign',)
    search_fields = ('title', 'slug',)
