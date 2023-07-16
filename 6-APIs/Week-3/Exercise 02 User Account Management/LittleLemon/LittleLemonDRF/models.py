from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)


class MenuItem(models.Model):
    title = models.SlugField()
    price = models.CharField(max_length=255)
    inventory = models.SmallIntegerField()

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)


class Rating(models.Model):
    menuitem_id = models.SmallIntegerField()
    rating = models.SmallIntegerField()

    category = models.ForeignKey(User, on_delete=models.CASCADE)
