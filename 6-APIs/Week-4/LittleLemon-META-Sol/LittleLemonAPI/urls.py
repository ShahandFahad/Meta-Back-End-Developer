from django.urls import path
from . import views

urlpatterns = [
    path("categories", views.CategoriesView.as_view()),
    path("menu-items", views.MenuItemsView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("cart/menu-items", views.CartView.as_view()),
    path("orders", views.OrderView.as_view()),
    path("orders/<int:pk>", views.SingleOrderView.as_view()),
    path(
        "groups/manager/users",
        views.GroupViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
    path(
        "groups/delivery-crew/users",
        views.DeliveryCrewViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
]
