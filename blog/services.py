from django.core.cache import cache

from blog.models import BlogPost
from mailing_list_service.settings import CACHE_ENABLED


def get_blog_posts_from_cash():
    """Функция получения активных постов из кэша"""
    if not CACHE_ENABLED:
        return BlogPost.objects.filter(is_published=True)
    key = 'blog_posts'
    blog_posts = cache.get(key)
    if blog_posts is not None:
        return blog_posts
    blog_posts = BlogPost.objects.filter(is_published=True)
    cache.set(key, blog_posts)
    return blog_posts
