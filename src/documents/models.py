from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
User = settings.AUTH_USER_MODEL

class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(default = "Title")
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #This would make the db auto update the field to when it is created
    updated_at = models.DateTimeField(auto_now=True) #This would make the db auto update the field when the doc is updated/edited
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(auto_now_add=False, auto_now=False, default = timezone.now, blank=True)