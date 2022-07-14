from tabnanny import verbose
from django.db import models
from apps.accounts.models import CustomUser
from django.urls import reverse


class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent_id = models.ForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self) -> str:
        return self.title


class Service(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL)
    detail = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):  # new
        return reverse('class-detail', args=[str(self.id)])

    def get_total_price(self, month):
        return month * self.price


class Image(models.Model):
    service = models.ForeignKey(Service, blank=True, null=True,
                                on_delete=models.SET_NULL, related_name='product_image')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')


class Comment(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField()
    rate = models.IntegerField(range(0, 6), default=0, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, blank=True,
                             null=True, on_delete=models.SET_NULL)
    ipaddress = models.GenericIPAddressField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
