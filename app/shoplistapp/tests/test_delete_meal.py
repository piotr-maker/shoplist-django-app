import pytest
from ..models import *


@pytest.fixture()
@pytest.mark.django_db
def test_create_meal():
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
def test_delete_meal(test_create_meal):
    meal = Meals.objects.get(id=1)
    meal.delete()

    assert len(Categories.objects.all()) == 1
    assert len(Meals.objects.all()) == 0
    assert len(MealsIngredients.objects.all()) == 0
    assert len(Ingredients.objects.all()) == 2
    assert len(Units.objects.all()) == 2
