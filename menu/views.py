from django.shortcuts import render

# Create your views here.

from .models import FoodItem, DrinkItem


def menus(request, 'menus_page.html')


class FoodMenu(generic.ListView):

    model = FoodItem
    template_name = 'food_menu.html'
    context_object_name = 'food_items'


def get_queryset(self):
    queryset = {
        'dinner_items': FoodItem.objects.all().filter(
            on_menu=True, food_menu_section=0
        ),
        'desserts': FoodItem.objects.all().filter(
            on_menu=True, food_menu_section=1
        ),
    }
    return queryset


class DrinksMenu(generic.ListView):

    model = DrinkItem
    template_name = 'drinks_menu_html'
    context_object_name = 'drinks_items'


def get_queryset(self):
    queryset = {
        'Cocktails_items': DrinkItem.objects.all().filter(
            on_menu=True, drink_menu_section=0
        ),
        'alcohol_items': DrinkItem.objects.all().filter(
            on_menu=True, drink_menu_section=1
        ),
        'softdrinks_item': DrinkItem.objects.all().filter(
            on_menu=True, drink_menu_section=2
        ),
    }
    return queryset
