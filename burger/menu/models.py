from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    burger_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


