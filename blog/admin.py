from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')
