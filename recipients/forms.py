from django import forms

from recipients.models import Recipients


class StyleFormMixin:
    """Стилизация форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RecipientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Recipients
        fields = '__all__'
