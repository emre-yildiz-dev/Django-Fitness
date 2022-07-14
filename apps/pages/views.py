from django.views.generic import TemplateView, ListView
from apps.accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.settings.models import Setting


class HomePageView(ListView):
    model = Setting
    context_object_name = 'settings'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(pk=1)
        return context


class ProfilePageView(TemplateView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('home'))
