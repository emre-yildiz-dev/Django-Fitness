from django.db import models

class Faq(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
