# Generated by Django 5.0.4 on 2024-05-12 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_datetime', models.DateTimeField(auto_now_add=True, verbose_name='first_datetime')),
                ('end_time', models.DateTimeField(verbose_name='end_time')),
                ('sending_period', models.CharField(choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц')], max_length=50, verbose_name='sending_period')),
                ('settings_status', models.CharField(choices=[('Create', 'Создана'), ('Started', 'Отправляется'), ('Done', 'Завершена')], default='Create', max_length=50, verbose_name='settings_status')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingmessage', verbose_name='message')),
                ('recipients', models.ManyToManyField(to='recipients.recipients', verbose_name='recipients')),
            ],
            options={
                'verbose_name': 'Настройка отправки',
                'verbose_name_plural': 'Настройки отправки',
            },
        ),
        migrations.CreateModel(
            name='MailingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_datetime', models.DateTimeField(auto_now_add=True, verbose_name='last_datetime')),
                ('mailing_response', models.TextField(verbose_name='mailing_response')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='status')),
            ],
            options={
                'verbose_name': 'Статус отправки',
                'verbose_name_plural': 'Статусы отправки',
            },
        ),
    ]
