from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class extendeduser(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=20)
    unit = models.CharField(max_length=40)
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Asset(models.Model):
    IP_address = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    hosting_location = models.CharField(max_length=50)
    db_make_model = models.CharField(max_length=50)
    webserver = models.CharField(max_length=50, null=True)
    primary_role = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    billingcount = models.CharField(max_length=30)
    source = models.CharField(max_length=40)
    severity = models.CharField(max_length=10)
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hostname, self.hosting_location, self.user_email, self.severity

    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
        db_table = 'asset_table'
