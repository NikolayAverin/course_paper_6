from django.contrib import admin

from recipients.models import Recipients


@admin.register(Recipients)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')