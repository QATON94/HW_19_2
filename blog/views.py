from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'contents', 'preview', 'publication_sign')
    success_url = reverse_lazy('blog:blog_list')

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
    success_url = reverse_lazy('bkig:blog_view')

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('blog:blog_view', kwargs={'slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


def toggle_active(request, pk):
    student_item = get_object_or_404(Blog, pk=pk)
    if student_item.publication_sign:
        student_item.publication_sign = False
    else:
        student_item.publication_sign = True

    student_item.save()

    return redirect(reverse('blog:blog_list'))
