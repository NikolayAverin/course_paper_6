from django.db import models

from recipients.models import Recipients
from users.models import User

FREQUENCY_CHOICES = [('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц'), ]
STATUS_OF_NEWSLETTER = [("Create", 'Создана'), ("Started", 'Отправляется'), ("Done", 'Завершена'), ("Cancel", 'Отменена'), ]


class MailingMessage(models.Model):
    """Модель сообщения"""
    title = models.CharField(max_length=150, verbose_name='title')
    content = models.TextField(verbose_name='content')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='creator', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingSettings(models.Model):
    """Модель настроек отправки"""
    first_datetime = models.DateTimeField(verbose_name='first_datetime')
    next_datetime = models.DateTimeField(verbose_name='next_datetime', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='end_time')
    sending_period = models.CharField(max_length=50, verbose_name='sending_period', choices=FREQUENCY_CHOICES)
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name='message')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='creator', null=True, blank=True)
    settings_status = models.CharField(max_length=50, verbose_name='settings_status', choices=STATUS_OF_NEWSLETTER, default='Create')
    recipients = models.ManyToManyField(Recipients, verbose_name='recipients')

    def __str__(self):
        return f'{self.message} отправляется каждый {self.sending_period} с {self.first_datetime} для {self.recipients}'

    class Meta:
        verbose_name = 'Настройка отправки'
        verbose_name_plural = 'Настройки отправки'
        permissions = [
            ('can_see_mailing_settings', 'can see all mailing settings'),
            ('can_change_settings_status', 'can change settings status')
        ]


class MailingStatus(models.Model):
    """Модель статуса отправки"""
    last_datetime = models.DateTimeField(auto_now_add=True, verbose_name='last_datetime')
    status = models.CharField(max_length=50, verbose_name='статус попытки')
    mailing_response = models.TextField(verbose_name='mailing_response')
    mailing_id = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='mailing_id', null=True, blank=True)

    def __str__(self):
        return f'{self.status} отправлялось {self.last_datetime}, ответ сервера: {self.mailing_response}'

    class Meta:
        verbose_name = 'Статус отправки'
        verbose_name_plural = 'Статусы отправки'
