# Generated by Django 5.0.4 on 2024-05-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipients',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
