from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Member(models.Model):
    username=models.CharField(max_length=150)
    age=models.PositiveIntegerField(
        validators=[MinValueValidator(25),MaxValueValidator(95)])
    job=models.CharField(max_length=150)

    def __str__(self):
        return self.username



