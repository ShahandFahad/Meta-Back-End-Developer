from django.forms import ModelForm
from .models import Booking, Menu


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
