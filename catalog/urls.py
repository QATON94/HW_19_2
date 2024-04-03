from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contacts, name='contacts'),
    path('product/', product, name='product'),
    path('product/<int:pk>', views.product, name='product'),
]
