from django.db import models
from django.contrib.auth.models import User


class extendeduser(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=20)
    unit = models.CharField(max_length=40)
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
