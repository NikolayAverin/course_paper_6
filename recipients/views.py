from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from recipients.models import Recipients


class RecipientCreateView(CreateView):
    model = Recipients
    fields = ['email', 'name', 'description']
    success_url = reverse_lazy('recipients:list')


class RecipientListView(ListView):
    model = Recipients


class RecipientUpdateView(UpdateView):
    model = Recipients
    fields = ['email', 'name', 'description']
    success_url = reverse_lazy('recipients:list')


class RecipientDeleteView(DeleteView):
    model = Recipients
    success_url = reverse_lazy('recipients:list')


class RecipientDetailView(DetailView):
    model = Recipients
