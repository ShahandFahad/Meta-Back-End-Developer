from .models import MenuItems
from rest_framework import serializers


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        # fileds = ["id", "title", "price" "inventory"] # depricated
        fields = "__all__"
        extra_kwargs = {"price": {"min_value": 2}, "inventory": {"min_value": 0}}
