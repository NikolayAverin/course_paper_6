# Generated by Django 5.0.4 on 2024-05-12 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_alter_mailingstatus_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailingstatus',
            name='next_datetime',
        ),
    ]
