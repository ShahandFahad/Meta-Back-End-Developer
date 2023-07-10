from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    drink_price = models.IntegerField()


    def __str__(self):
        return self.drink