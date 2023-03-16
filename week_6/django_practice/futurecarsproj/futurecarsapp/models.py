from django.db import models

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=200)
    evil = models.BooleanField(default=True)

class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=200, default='NULL')
    does_fly = models.BooleanField(default=False)