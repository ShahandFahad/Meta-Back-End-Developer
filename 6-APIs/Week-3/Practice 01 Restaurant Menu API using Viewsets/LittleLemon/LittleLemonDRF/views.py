from django.shortcuts import render
from .models import MenuItems
from .serializers import MenuItemSerializer
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItems.objects.all()
#     serializer_class = MenuItemSerializer


# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MenuItems.objects.all()
#     serializer_class = MenuItemSerializer


class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ["price", "inventory"]
    search_fields = ["title"]
    # Search in nested files
    search_fields = ["title", "category__title"]
