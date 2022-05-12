from rest_framework import serializers
from .models import *


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


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
    class Meta:
        model = Meals

    def to_representation(self, instance):
        representation = dict()
        representation['id'] = instance.id
        representation['name'] = instance.name
        representation['category'] = instance.category_id.name
        return representation


class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Meals
        fields = ['id', 'name', 'servings', 'recipe', 'ingredients']
