from django.contrib import admin
from apps.faqs.models import Faq


class FaqsAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "created_at", "updated_at")


admin.site.register(Faq, FaqsAdmin)
