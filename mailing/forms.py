from django import forms

from mailing.models import MailingMessage, MailingSettings


class StyleFormMixin:
    """Стилизация форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingMessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingMessage
        exclude = ['creator']


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingSettings
        exclude = ['next_datetime', 'settings_status', 'creator']


class MailingSettingsModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('settings_status', )
