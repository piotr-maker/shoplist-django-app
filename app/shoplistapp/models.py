from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Meals(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.TextField()
    servings = models.IntegerField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

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
    meal_id = models.ForeignKey(Meals, related_name='ingredients', on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Units, related_name='unit', on_delete=models.CASCADE)
    quantity = models.IntegerField()

