from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""
    def handle(self, *args, **kwargs):
        user = User.objects.create(email='admin@example.com')
        user.set_password('adminadmin')
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
