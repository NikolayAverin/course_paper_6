from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingUpdateView, MailingDeleteView, MailingListView, MailingDetailView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='list'),
    path('create/', MailingCreateView.as_view(), name='create'),
    path('<int:pk>/', MailingDetailView.as_view(), name='view'),
    path('<int:pk>/update/', MailingUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', MailingDeleteView.as_view(), name='delete'),
]
