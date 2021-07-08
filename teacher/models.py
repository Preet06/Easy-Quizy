from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


class test_create(models.Model):
      test_code =  models.ForeignKey('auth.User',on_delete=models.CASCADE, )
      question = models.TextField()
      op1 = models.TextField()
      op2 = models.TextField()
      op3 = models.TextField()
      op4 = models.TextField()
      ans = models.TextField()

      def __str__(self):
            return self.question

      def get_absolute_url(self):  # new
            return reverse('home2')

