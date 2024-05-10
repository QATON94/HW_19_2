from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'contents', 'created_at', 'publication_sign', 'owner')
    list_filter = ('publication_sign',)
    search_fields = ('title', 'slug',)
