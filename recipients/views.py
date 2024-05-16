from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from recipients.forms import RecipientForm
from recipients.models import Recipients


class RecipientCreateView(CreateView):
    model = Recipients
    form_class = RecipientForm
    success_url = reverse_lazy('recipients:list')


class RecipientListView(ListView):
    model = Recipients


class RecipientUpdateView(UpdateView):
    model = Recipients
    form_class = RecipientForm
    success_url = reverse_lazy('recipients:list')


class RecipientDeleteView(DeleteView):
    model = Recipients
    success_url = reverse_lazy('recipients:list')


class RecipientDetailView(DetailView):
    model = Recipients
