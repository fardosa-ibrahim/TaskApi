from django.db import models

# Create your models here.
class User(models.Model):
    slackUsername = models.CharField(max_length=10, null = True)
    backend = models.BooleanField(max_length=10, null = True)
    Age = models.IntegerField()