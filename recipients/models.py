from django.db import models

from users.models import User


class Recipients(models.Model):
    """Модель получателей рассылки"""
    email = models.EmailField(verbose_name='email', unique=True)
    name = models.CharField(max_length=150, verbose_name='name')
    description = models.TextField(blank=True, null=True, verbose_name='description')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
