from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Shoe(models.Model):
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shoe/', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    def str(self):
        return self.brand