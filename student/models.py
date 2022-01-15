from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse
from account.models import *
from django.utils import timezone
from teacher.models import *


# Create your models here.


class Program(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    lab_cycle=models.ForeignKey(Lab_cycle,on_delete=models.CASCADE,null=True,blank=True)
    program_name=models.CharField(max_length=50)
    program_file=models.FileField(upload_to='programs')
    mark=models.CharField(max_length=20,null=True,blank=True)
    due=models.BooleanField(default=False)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.program_name)
