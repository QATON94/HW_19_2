from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_active

app_name = BlogConfig.name

urlpatterns = [
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog_view/<slug:slug>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_edit/<slug:slug>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
    path('activity/<int:pk>/', toggle_active, name='toggle_active'),
]
