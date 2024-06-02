from django import forms
from django.forms import BooleanField

from blog.models import BlogPost


class StyleFormMixin:
    """Стилизация формы"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class BlogPostForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'image')


class BlogPostModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('is_published',)
