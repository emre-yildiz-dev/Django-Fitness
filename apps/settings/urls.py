from django.urls import path
from .views import AboutUsPageView, ContactUsPageView

urlpatterns = [
    path('about-us', AboutUsPageView.as_view(), name='about-us'),
    path('contact-us', ContactUsPageView.as_view(), name='contact-us'),
]