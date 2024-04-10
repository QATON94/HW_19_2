from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product



class HomeListView(ListView):
    template_name = 'catalog/home.html'
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            massage = request.POST.get('message')
            print(f"Имя: {name}, Телефон: {phone}, Сообщение: {massage}")
        return render(request, 'catalog/contacts.html')


class ProductListView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


