from django.db import models

# Create your models here.
class user(models.Model):
    id = models.IntegerField()
    name = models.CharField()