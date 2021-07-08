from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class student_info(models.Model):
    roll_no = models.IntegerField()
    marks = models.IntegerField()
