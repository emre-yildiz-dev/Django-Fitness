from django.db import models
from ckeditor.fields import RichTextField


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=254)
    keywords = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    company = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    smtpserver = models.CharField(max_length=254)
    smtpemail = models.EmailField(max_length=254)
    smtppassword = models.CharField(max_length=254)
    smtpport = models.IntegerField()
    facebook = models.CharField(max_length=254)
    instagram = models.CharField(max_length=254)
    twitter = models.CharField(max_length=254)
    aboutus = models.TextField()
    contact = models.CharField(max_length=254)
    references = RichTextField()
    status = models.CharField(max_length=10, choices=STATUS)
