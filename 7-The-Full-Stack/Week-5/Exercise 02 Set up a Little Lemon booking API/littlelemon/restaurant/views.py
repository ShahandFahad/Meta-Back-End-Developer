from django.http import HttpResponse
from django.shortcuts import render

from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from .forms import BookingForm


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


# Add code for the bookings() view
def bookings(request):
    date = request.GET.get("date", datetime.today().date)
    bookings = Booking.objects.all()
    booking_json = serializers.serialize("json", bookings)

    # return render(request, "bookings.html", {"bookings": booking_json})

    bookings_data = {"bookings": bookings}
    return render(request, "bookings.html", {"bookings": bookings_data})


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})
