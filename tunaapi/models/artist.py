from django.db import models

class Artist(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    bio = models.CharField(max_length=50)
