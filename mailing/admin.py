from django.contrib import admin

from mailing.models import MailingMessage, MailingSettings


@admin.register(MailingMessage)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'creator')


@admin.register(MailingSettings)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_datetime', 'message', 'creator')
