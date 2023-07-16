from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticated

from .models import MenuItem, Rating
from .serializers import MenuItemSerializer, RatingSerializer


class MenuItemsViewSet(viewsets.ModelViewSet):
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_throttles(self):
        if self.action == "create":
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []
        return [throttle() for throttle in throttle_classes]


class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []

        return [IsAuthenticated()]
