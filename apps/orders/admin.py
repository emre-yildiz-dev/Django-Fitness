from django.contrib import admin
from apps.orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "service", "months", "total")


admin.site.register(Order, OrderAdmin)
