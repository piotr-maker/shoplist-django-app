from .models import *
from .serializers import *
from rest_framework import generics, response
from django.http import Http404


class CategoriesList(generics.ListAPIView):
    """
    Wyświetl kategorie posiłków
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class MealsList(generics.ListAPIView):
    """
    Wyświetl wszystkie posiłki
    """
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class MealsByCategory(generics.ListAPIView):
    """
    Wyświetl posiłki z podziałem na kategorię
    """
    serializer_class = MealsSerializer
    
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if not Categories.objects.filter(id=category_id).exists():
            raise Http404()

        return Meals.objects.filter(
            category_id=category_id
        )


class MealDetail(generics.RetrieveAPIView):
    """
    Wyświetl szczegóły posiłku: przepis, listę składników
    """
    lookup_field = 'id'
    serializer_class = MealSerializer

    def get_queryset(self):
        meal_id = self.kwargs.get('id')
        if not Meals.objects.filter(id=meal_id).exists():
            raise Http404()

        return Meals.objects.filter(
            id=meal_id
        )


class IngredientList(generics.ListAPIView):
    serializer_class = IngredientSerializer

    def search(self, ingredients, ingredient):
        for i in range(len(ingredients)):
            if ingredients[i].ingredient == ingredient.ingredient:
                return i
        return -1

    def create_list(self, meal_ids):
        result = []
        for ingredient in MealsIngredients.objects.filter(meal_id__in=meal_ids).order_by('ingredient'):
            index = self.search(result, ingredient)
            if index >= 0:
                result[index].quantity += ingredient.quantity
            else:
                result.append(ingredient)
        return result

    def get(self, request, *args, **kwargs):
        meals = request.GET.getlist('meal')
        for i in range(0, len(meals)):
            meals[i] = int(meals[i])
        ingredients = self.create_list(meals)
        data = self.get_serializer(ingredients, many=True).data
        return response.Response({'ingredients':data})
