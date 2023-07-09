from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.about, name='menu'),
    path('book/', views.book, name='book')
]