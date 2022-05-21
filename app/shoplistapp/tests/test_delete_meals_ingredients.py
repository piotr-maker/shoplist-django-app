import pytest
from ..models import *


@pytest.fixture()
@pytest.mark.django_db
def test_create_meal_ingredient():
    category = Categories.objects.create(name="diner")
    category.save()
    meal = Meals.objects.create(name="chicken soup", recipe="recipe", servings=1, category=category)
    meal.save()

    unit = Units.objects.create(name="piece")
    unit.save()
    ingredient = Ingredients.objects.create(name="carrot")
    ingredient.save()
    mi = MealsIngredients.objects.create(meal=meal, unit=unit, ingredient=ingredient, quantity=2)
    mi.save()

    unit = Units.objects.create(name="clove")
    unit.save()
    ingredient = Ingredients.objects.create(name="garlic")
    ingredient.save()
    mi = MealsIngredients.objects.create(meal=meal, unit=unit, ingredient=ingredient, quantity=6)
    mi.save()

    assert len(Categories.objects.all()) == 1
    assert len(Meals.objects.all()) == 1
    assert len(MealsIngredients.objects.all()) == 2


@pytest.mark.django_db
def test_delete_one_meal_ingredient(test_create_meal_ingredient):
    mi = MealsIngredients.objects.get(id=1)
    mi.delete()

    assert len(Categories.objects.all()) == 1
    assert len(Meals.objects.all()) == 1
    assert len(MealsIngredients.objects.all()) == 1
    assert len(Ingredients.objects.all()) == 2
    assert len(Units.objects.all()) == 2


@pytest.mark.django_db
def test_delete_all_meal_ingredients(test_create_meal_ingredient):
    meal_ingredients = MealsIngredients.objects.all()
    for meal_ingredient in meal_ingredients:
        meal_ingredient.delete()

    assert len(Categories.objects.all()) == 1
    assert len(Meals.objects.all()) == 1
    assert len(MealsIngredients.objects.all()) == 0
    assert len(Ingredients.objects.all()) == 2
    assert len(Units.objects.all()) == 2
