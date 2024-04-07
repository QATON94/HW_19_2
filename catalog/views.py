from datetime import datetime
from django.shortcuts import get_object_or_404, redirect

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog

from pytils.translit import slugify


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


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'contents', 'preview', 'publication_sign')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        blog = form.save()
        blog.slug = slugify(f'{blog.title}-{datetime.now().strftime("%Y-%m-%d")}')
        blog.save()
        return HttpResponseRedirect(str(self.success_url))


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.numbers_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'contents', 'preview', 'publication_sign')
    success_url = reverse_lazy('catalog:blog_view')

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('catalog:blog_view', kwargs={'slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')

def toggle_active(request, pk):
    student_item = get_object_or_404(Blog, pk=pk)
    if student_item.publication_sign:
        student_item.publication_sign = False
    else:
        student_item.publication_sign = True

    student_item.save()

    return redirect(reverse('catalog:blog_list'))
