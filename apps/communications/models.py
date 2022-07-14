from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=254)
    message = models.CharField(max_length=254)
    ipaddress = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
