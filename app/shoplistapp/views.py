from .models import *
from .serializers import *
from rest_framework import generics
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

