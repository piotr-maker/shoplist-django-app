from django.db import models


class Meals(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.TextField()

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Units(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MealsIngredients(models.Model):
    meal_id = models.ForeignKey(Meals, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Units, on_delete=models.CASCADE)
    quantity = models.IntegerField()

