from django.urls import path
from .views import message_post

urlpatterns = [
    path('message_post', message_post, name='message-post'),
]
