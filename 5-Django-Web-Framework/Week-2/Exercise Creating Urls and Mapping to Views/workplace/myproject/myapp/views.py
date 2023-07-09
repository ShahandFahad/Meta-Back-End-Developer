from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Little Lemon!</h2>", content_type="text/html", status=200)

# About View
def about(request):
    content = "<h1>About</h1>"
    return HttpResponse(content, content_type="text/html", status=200)

# Menu
def menu(request):
    content = "<h1>Menu</h1>"
    return HttpResponse(content, content_type="text/html", status=200)

# book
def book(request):
    content = "<h1>Book</h1>"
    return HttpResponse(content, content_type="text/html", status=200)
