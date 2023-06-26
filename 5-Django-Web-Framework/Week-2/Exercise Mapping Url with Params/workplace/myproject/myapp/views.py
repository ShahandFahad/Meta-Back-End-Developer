from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def drinks(request, drink_name):
    drink = {
        "mocha": "A Type of coffe",
        "tea": "A type of beverage",
        "lemonade": "A type of refereshment",
    }

    choice_of_drink = drink[drink_name]

    return HttpResponse(f"<h2> {drink_name} </h2>" + f"<h3> {choice_of_drink} </h3>")
