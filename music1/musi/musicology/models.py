from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Music(models.Model):
    singer=models.CharField(max_length=150)
    name=models.CharField(max_length=300)
    mugory=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    rating=models.FloatField(
        validators=[MinValueValidator(0),MaxValueValidator(5)]
    )
    image=models.ImageField(null=True)
    description=models.CharField(max_length=1500)
    file=models.FileField(null=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    email  = models.EmailField(("user email"), max_length=254)
    comment  = models.TextField()
    post  = models.ForeignKey(Music, on_delete=models.CASCADE)
    
