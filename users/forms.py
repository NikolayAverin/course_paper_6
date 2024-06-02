from django.contrib.auth.forms import UserCreationForm
from django import forms

from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'avatar')


class UserModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'is_active')
