from .models import MenuItems
from rest_framework import serializers
import bleach


class MenuItemSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        return bleach.clean(value)

    class Meta:
        model = MenuItems
        # fileds = ["id", "title", "price" "inventory"] # depricated
        fields = "__all__"
        extra_kwargs = {"price": {"min_value": 2}, "inventory": {"min_value": 0}}
