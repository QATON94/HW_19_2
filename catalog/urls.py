from django.urls import path

from catalog import views
from catalog.views import home, contacts, product

urlpatterns = [
    path('', home),
    path('contact/', contacts),
    path('product/', product),
    path('product/<int:pk>', views.product, name='product'),
]
