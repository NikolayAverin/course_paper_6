# Generated by Django 5.0.4 on 2024-05-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='first_datetime',
            field=models.DateTimeField(verbose_name='first_datetime'),
        ),
    ]
