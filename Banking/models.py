from django.db import models

class User(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=25)

    def __str__(self):
       return self.name



