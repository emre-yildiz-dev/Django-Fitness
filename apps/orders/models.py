from django.db import models
from apps.services.models import Service
from apps.accounts.models import CustomUser


class Order(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    PAYMENT = (
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card'),
    )
    user = models.ForeignKey(CustomUser, blank=True,
                             null=True, on_delete=models.SET_NULL)
    service = models.ForeignKey(
        Service, blank=True, null=True, on_delete=models.SET_NULL)
    StartDate = models.DateTimeField('order start date')
    EndDate = models.DateTimeField('order end date')
    months = models.CharField(max_length=50)  # think to refactor this field.
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    payment = models.CharField(
        blank=True, null=True, choices=PAYMENT, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default=False)
    ipaddress = models.GenericIPAddressField()
    note = models.CharField(max_length=254, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
