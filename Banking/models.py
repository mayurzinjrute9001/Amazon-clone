import random

from django.db import models

class User(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=25)
    acc_number=models.IntegerField(default=random.randint(0000000,9999999))
    acc_status=models.BooleanField(default=False)

    def __str__(self):
       return self.name



