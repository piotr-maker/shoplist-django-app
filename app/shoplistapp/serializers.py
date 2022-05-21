from rest_framework import serializers
from .models import *


class CategoriesSerializer(serializers.ModelSerializer):
    categories_endpoint = 'api/meals/categories/'
    url = serializers.CharField(source='', read_only=True)

    class Meta:
        model = Categories
        fields = ['name', 'url']

    def to_representation(self, instance):
        representation = dict()
        representation['name'] = instance.name
        representation['url'] = self.categories_endpoint + str(instance.id)
        return representation


class IngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.CharField(source='ingredient.name', read_only=True)
    unit = serializers.CharField(source='unit.name', read_only=True)

    class Meta:
        model = MealsIngredients
        fields = ['ingredient', 'quantity', 'unit']


class MealsSerializer(serializers.ModelSerializer):
    app_endpoint = 'api/meals/'
    category = serializers.CharField(source='category.name', read_only=True)
    url = serializers.CharField(source='', read_only=True)

    class Meta:
        model = Meals
        fields = ['id', 'name', 'servings', 'category', 'url']

    def to_representation(self, instance):
        representation = dict()
        representation['id'] = instance.id
        representation['name'] = instance.name
        representation['servings'] = instance.servings
        representation['category'] = instance.category.name
        representation['url'] = self.app_endpoint + str(instance.id)
        return representation


class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Meals
        fields = ['id', 'name', 'servings', 'recipe', 'ingredients']
