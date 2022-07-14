from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'ipaddress')


admin.site.register(Message, MessageAdmin)
