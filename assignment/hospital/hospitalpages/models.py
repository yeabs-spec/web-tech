from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Department(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
class Hospital(models.Model):
    user=models.CharField(max_length=100)
    field=models.CharField(max_length=100)
    age=models.PositiveIntegerField(
        validators=[MinValueValidator(23),MaxValueValidator(100)])
    Proffesion=models.CharField(max_length=150)
    image=models.ImageField(null=True)
    dr_department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.user
    