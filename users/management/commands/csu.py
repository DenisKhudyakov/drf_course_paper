from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Класс для создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@admin.ru",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password("qwe123")
        user.save()
