from django.contrib import admin
# Import the models from models.py
from .models import Drinks, DrinksCategory

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
