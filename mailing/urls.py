from django.urls import path

from recipients.apps import RecipientsConfig
from recipients.views import RecipientListView, RecipientCreateView, RecipientDetailView, RecipientUpdateView, \
    RecipientDeleteView

app_name = RecipientsConfig.name

urlpatterns = [
    path('recipients/', RecipientListView.as_view(), name='list'),
    path('recipients/create/', RecipientCreateView.as_view(), name='create'),
    path('recipients/<int:pk>/', RecipientDetailView.as_view(), name='view'),
    path('recipients/<int:pk>/update/', RecipientUpdateView.as_view(), name='edit'),
    path('recipients/<int:pk>/delete/', RecipientDeleteView.as_view(), name='delete'),
]
