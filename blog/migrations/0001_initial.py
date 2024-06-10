# Generated by Django 4.2.2 on 2024-06-02 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='image')),
                ('views_count', models.IntegerField(default=0, verbose_name='views_count')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
    ]