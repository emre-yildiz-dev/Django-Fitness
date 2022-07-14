from email.mime import image
from email.policy import default
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class CustomUser(AbstractUser):
    is_member = models.BooleanField(default=False)
    avatar = models.ImageField(
        upload_to='images/', blank=True, null=True, default="images/avatar.jpeg")
    street = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(blank=True, max_length=255)
    remark = RichTextField(blank=True, null=True)
