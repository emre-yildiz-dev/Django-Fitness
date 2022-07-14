from django.urls import path
from apps.faqs.views import get_faqs

urlpatterns = [
    path('', get_faqs, name='get-faqs'),
]
