from django.db import models

# Create your models here.

class emailAddr(models.Model):
    emailaddr = models.CharField(max_length=100)
    emailpsd = models.CharField(max_length=100)