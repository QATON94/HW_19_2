from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='godslayer94@yandex.ru',
            is_active=True,
            is_staff=True,
            is_superuser=True,
            country='Россия',
            phone_number='+7 999 999 99 99'
        )

        user.set_password('admin')
        user.save()
