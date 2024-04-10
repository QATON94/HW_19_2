from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ProductListView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contact/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductListView.as_view(), name='product'),
]
