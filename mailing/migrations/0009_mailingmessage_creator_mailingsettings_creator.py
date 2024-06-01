# Generated by Django 4.2.2 on 2024-06-01 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0008_mailingsettings_next_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingmessage',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
    ]