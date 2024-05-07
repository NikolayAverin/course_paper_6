from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailing.models import MailingMessage


class MailingCreateView(CreateView):
    model = MailingMessage
    fields = ['title', 'content', 'recipients']
    success_url = reverse_lazy('mailing:list')


class MailingUpdateView(UpdateView):
    model = MailingMessage
    fields = ['title', 'content','recipients']
    success_url = reverse_lazy('mailing:list')


class MailingDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:list')


class MailingListView(ListView):
    model = MailingMessage


class MailingDetailView(DetailView):
    model = MailingMessage
