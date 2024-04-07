from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ProductListView, ContactsView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView, toggle_active

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contact/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductListView.as_view(), name='product'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_view/<slug:slug>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_edit/<slug:slug>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_edit/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
    path('activity/<int:pk>/', toggle_active, name='toggle_active'),
]
