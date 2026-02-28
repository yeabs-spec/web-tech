from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    contact = models.IntegerField

class category(models.Model):
    name = models.CharField(max_length=200)

class event(models.Model):
    AGE_LIMIT = [
        (0,"all ages"),
        (13,"13+"),
        (18,"18+"),
    ]
    name = models.CharField(max_length=200)
    starting_time=models.DateTimeField()
    ending_time=models.DateTimeField()
    event_address=models.CharField(max_length=1000)

