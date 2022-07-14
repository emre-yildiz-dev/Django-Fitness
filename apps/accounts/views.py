from django.urls import reverse_lazy
from django.views import generic
from apps.accounts.models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


@login_required
def update_user(request):
    print(request.POST)
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.street = request.POST.get('address')
        user.city = request.POST.get('city')
        user.state = request.POST.get('state')
        user.username = request.POST.get('username')
        print(request.POST)
        if(request.POST.get('password') == request.POST.get('confirmPassword')):
            user.set_password(request.POST.get('password'))
        user.save()
        return render(request, "account/profile.html")
