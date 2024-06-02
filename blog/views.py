from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogPostForm, BlogPostModeratorForm
from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """Сохранение автора записи"""
        blog_post = form.save()
        user = self.request.user
        blog_post.author = user
        blog_post.save()
        return super().form_valid(form)


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        """Вывод только активных записей"""
        return super().get_queryset().filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        """Увеличение количества просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        """Перенаправление на просмотр записи после редактирования"""
        return reverse('blog:view', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        """Переопределяем форму для модератора"""
        user = self.request.user
        if user == self.object.author:
            return BlogPostForm
        if user.has_perm('blog.can_unpublished'):
            return BlogPostModeratorForm
        raise PermissionDenied


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:list')
