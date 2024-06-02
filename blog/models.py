from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    content = models.TextField(verbose_name='content')
    image = models.ImageField(upload_to='blog', verbose_name='image', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='views_count')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='author', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='is_published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        permissions = [
            ('can_unpublished', 'can unpublished')
        ]
