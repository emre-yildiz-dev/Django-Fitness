from django.urls import path

from apps.accounts.models import CustomUser
from .views import SignupPageView
from apps.accounts.views import update_user

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('update-user/', update_user, name='profile.html'),
]
