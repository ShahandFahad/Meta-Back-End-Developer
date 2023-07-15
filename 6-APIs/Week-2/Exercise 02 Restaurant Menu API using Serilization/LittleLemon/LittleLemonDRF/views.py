from django.shortcuts import render
from .models import MenuItems
from .serializers import MenuItemSerializer
from rest_framework import generics


# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
