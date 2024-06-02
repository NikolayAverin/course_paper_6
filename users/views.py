import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from users.forms import UserRegisterForm, UserForm, UserModeratorForm
from users.models import User
from mailing_list_service.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Отправка письма для верификации почты"""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения почты перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Подтверждение почты"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('mailing:settings_list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('users.can_deactivate_user'):
            return UserModeratorForm
        if user == self.request.user:
            return UserForm
        raise PermissionDenied

    def get_object(self, queryset=None):
        """Получаем текущего пользователя"""
        return self.request.user


class UserListView(LoginRequiredMixin, ListView):
    model = User


def change_activity(request, pk):
    """Изменение активности пользователя"""
    user = User.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect('users:users_list')
