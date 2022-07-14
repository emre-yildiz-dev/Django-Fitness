from django.views.generic import TemplateView, ListView
from apps.settings.models import Setting


class AboutUsPageView(ListView):
    model = Setting
    context_object_name = 'settings'
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsPageView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(pk=1)
        return context


class ContactUsPageView(TemplateView):
    template_name = 'contact-us.html'
