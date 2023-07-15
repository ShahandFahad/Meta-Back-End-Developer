from django.urls import path
from . import views

urlpatterns = [
    path("books", views.Books),
    # path('books/<int:pk>',views.book),
]
