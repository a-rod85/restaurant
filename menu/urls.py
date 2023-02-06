from menus import views
from django.urls import path, include

urlpatterns [
    path("", views.menu, name='menu'),
    path('food_menu', views.FoodMenu.as_view(), name='food_menu'),
    path('drnks_menu', views.DrinksMenu.as_view(), name='drinks_menu'),
]
