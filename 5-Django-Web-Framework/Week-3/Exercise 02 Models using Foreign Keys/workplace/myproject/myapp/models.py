from django.db import models

# Create your models here.

# Create model DrinksCategory 
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

# Create model Drinks
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()

    # Foreign key relate to drinks category
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)

