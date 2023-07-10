from django import forms
from .models import Booking

# model form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"