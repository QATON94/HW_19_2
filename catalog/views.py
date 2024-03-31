from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        massage = request.POST.get('message')
        print(f"Имя: {name}, Телефон: {phone}, Сообщение: {massage}")
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    product = Product.objects.get(pk=pk)
    # context = {
    #     'category': Product.objects.all()
    # }
    return render(request, 'catalog/product.html')
