from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = PhoneNumberField(verbose_name='phone', **NULLABLE)
    avatar = models.ImageField(upload_to='users', verbose_name='avatar', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='token', **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('can_see_users_list', 'can see all users'),
            ('can_deactivate_user', 'can deactivate user')
        ]
