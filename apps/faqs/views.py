from django.shortcuts import render
from apps.faqs.models import Faq


def get_faqs(request):
    faq_list = Faq.objects.filter(status=True)
    context = {
        'faq_list': faq_list
    }
    return render(request, 'faqs.html', context)
