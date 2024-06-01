from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailing.forms import MailingMessageForm, MailingSettingsForm, MailingSettingsModeratorForm
from mailing.models import MailingMessage, MailingSettings, MailingStatus


class MailingMessageCreateView(CreateView, LoginRequiredMixin):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        """Сохранение создателя сообщения"""
        mailing_message = form.save()
        user = self.request.user
        mailing_message.creator = user
        mailing_message.save()
        return super().form_valid(form)


class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:list')


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:list')


class MailingMessageListView(ListView):
    model = MailingMessage


class MailingMessageDetailView(DetailView):
    model = MailingMessage


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')

    def form_valid(self, form):
        """Сохранение создателя сообщения"""
        mailing_settings = form.save()
        user = self.request.user
        mailing_settings.creator = user
        mailing_settings.save()
        return super().form_valid(form)


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')

    def get_form_class(self):
        """Переопределяем форму для модератора"""
        user = self.request.user
        if user == self.object.creator:
            return MailingSettingsForm
        if user.has_perm('mailing.can_change_settings_status'):
            return MailingSettingsModeratorForm
        raise PermissionDenied


class MailingSettingsListView(ListView):
    model = MailingSettings


class MailingSettingsDetailView(DetailView):
    model = MailingSettings


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:settings_list')


class MailingStatusListView(ListView):
    model = MailingStatus


class MailingStatusDeleteView(DeleteView):
    model = MailingStatus
    success_url = reverse_lazy('mailing:status_list')
