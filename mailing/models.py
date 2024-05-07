from django.db import models


class MailingMessage(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    content = models.TextField(verbose_name='content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingSettings(models.Model):
    first_datetime = models.DateTimeField(auto_now_add=True, verbose_name='first_datetime')
    sending_period = models.DateTimeField(verbose_name='sending_period')
    status = models.CharField(max_length=50, verbose_name='status')
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name='message')
    recipients = models.ManyToManyField('recipients.Recipients', verbose_name='recipients')

    def __str__(self):
        return f'{self.message} отправляется каждый {self.sending_period} с {self.first_datetime}'

    class Meta:
        verbose_name = 'Настройка отправки'
        verbose_name_plural = 'Настройки отправки'


class MailingStatus(models.Model):
    last_datetime = models.DateTimeField(auto_now_add=True, verbose_name='last_datetime')
    status = models.BooleanField(default=False, verbose_name='status')
    mailing_response = models.TextField(verbose_name='mailing_response')

    def __str__(self):
        return f'{self.status} отправлялось {self.last_datetime}, ответ сервера: {self.mailing_response}'

    class Meta:
        verbose_name = 'Статус отправки'
        verbose_name_plural = 'Статусы отправки'
