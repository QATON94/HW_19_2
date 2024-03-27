import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data/catalog_data.json', encoding='utf-8') as f:
            file_data = json.load(f)
            categories = []
            for item in file_data:
                if item['model'] == 'catalog.category':
                    categories.append(item)
            return categories

    @staticmethod
    def json_read_products():
        with open('data/catalog_data.json', encoding='utf-8') as f:
            file_data = json.load(f)
            products = []
            for item in file_data:
                if item['model'] == 'catalog.product':
                    products.append(item)
            return products

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()
        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], name=category["fields"]['name'],
                         description=category["fields"]['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'], name=product["fields"]['name'],
                        description=product["fields"]['description'], picture=product["fields"]['picture'],
                        category=Category.objects.get(pk=product["fields"]['category']),
                        price_for_purchase=product["fields"]['price_for_purchase'],
                        created_at=product["fields"]['created_at'],
                        updated_at=product["fields"]['updated_at'])
            )

            # Создаем объекты в базе с помощью метода bulk_create()
            Product.objects.bulk_create(product_for_create)
