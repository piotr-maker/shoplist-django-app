from rest_framework import serializers
from .models import *


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ['id', 'name']


class MealSerializer(serializers.ModelSerializer):
    meals = serializers.StringRelatedField(many=False)

    class Meta:
        model = MealsIngredients
        fields = ['id', 'quantity']
