# Generated by Django 5.0.4 on 2024-05-07 16:13

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
            name='MailingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_datetime', models.DateTimeField(auto_now_add=True, verbose_name='last_datetime')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('mailing_response', models.TextField(verbose_name='mailing_response')),
            ],
            options={
                'verbose_name': 'Статус отправки',
                'verbose_name_plural': 'Статусы отправки',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_datetime', models.DateTimeField(auto_now_add=True, verbose_name='first_datetime')),
                ('sending_period', models.DateTimeField(verbose_name='sending_period')),
                ('status', models.CharField(max_length=50, verbose_name='status')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingmessage', verbose_name='message')),
                ('recipients', models.ManyToManyField(to='recipients.recipients', verbose_name='recipients')),
            ],
            options={
                'verbose_name': 'Настройка отправки',
                'verbose_name_plural': 'Настройки отправки',
            },
        ),
    ]
