# Generated by Django 4.2.2 on 2024-06-01 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0009_mailingmessage_creator_mailingsettings_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsettings',
            options={'permissions': [('can_see_mailing_settings', 'can see all mailing settings'), ('can_change_settings_status', 'can change settings status')], 'verbose_name': 'Настройка отправки', 'verbose_name_plural': 'Настройки отправки'},
        ),
    ]
