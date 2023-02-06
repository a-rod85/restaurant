from django.db import models


Food_Menu_Section = ((0, 'Dinner'), (1, 'Desserts'),)
Drinks_Menu_Section = (
    (0, 'Cocktails'),
    (1, 'Wines/Beers'),
    (2, 'Soft Drinks'),
)

# Create your models here.


class FoodItem(models.Model):

    dish_id = models.AutoField(primary_key=True)
    dish_name = models.Charfield(max_length=220, unique=True)
    description = models.Charfield(max_length=220, unique=True)
    price = models.FloatField()
    Food_Menu_Section = models.IntergerField(
        choices=Food_Menu_Section, default=1)
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['on_menu']

    def __str__(self):
        return self.dish_name


class DrinkItem(models.Model):

    drink_id = models.AutoField(primary_key=True)
    drink_name = maodels.Charfield(max_length=100, unique=True)
    description = models.Charfield(max_length=200, unique=True)
    price = models.FloatField()
    Drink_menu_section = models.IntergerField(
        choices=Food_Menu_Section, default=1)
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['on_menu']

    def __str__(self):
        return self.drink_name
