from rest_framework import serializers
from .models import *


class CategoriesSerializer(serializers.ModelSerializer):
    categories_endpoint = 'api/meals/categories/'
    class Meta:
        model = Categories

    def to_representation(self, instance):
        representation = dict()
        representation['name'] = instance.name
        representation['url'] = self.categories_endpoint + str(instance.id)
        return representation


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsIngredients

    def to_representation(self, instance):
        representation = dict()
        representation['ingredient'] = instance.ingredient_id.name
        representation['quantity'] = instance.quantity
        representation['unit'] = instance.unit_id.name
        return representation


class MealsSerializer(serializers.ModelSerializer):
    app_endpoint = 'api/meals/'
    class Meta:
        model = Meals

    def to_representation(self, instance):
        representation = dict()
        representation['id'] = instance.id
        representation['name'] = instance.name
        representation['servings'] = instance.servings
        representation['category'] = instance.category_id.name
        representation['url'] = self.app_endpoint + str(instance.id)
        return representation


class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Meals
        fields = ['id', 'name', 'servings', 'recipe', 'ingredients']
