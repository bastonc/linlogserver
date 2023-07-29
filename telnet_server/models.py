from django.db import models
from django.utils import timezone


# Create your models here.
class Chek_update(models.Model):
    version = models.CharField(max_length=50)
    timestamp = models.DateTimeField("Time request", default=timezone.now())
    call = models.CharField(max_length=10)

class Register_new (models.Model):
    call = models.CharField(max_length=10)
    timestamp = models.DateTimeField("Time-register")
    version = models.CharField(max_length=50)

class Version(models.Model):
    timestamp = models.DateTimeField("Time_new")
    version = models.CharField(max_length=10)
    github_path = models.CharField(max_length=255)
    enable = models.BooleanField(default=False)

class Template(models.Model):
    page_name = models.CharField(max_length=300)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    footer = models.fields.TextField(max_length=1000)
    h1 = models.CharField(max_length=300)
    content_left_panel = models.TextField(max_length=10000)
    content_right_panel = models.TextField(max_length=10000)
    timestamp = models.DateTimeField("Time edit")

class Admins(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
