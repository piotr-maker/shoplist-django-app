from .models import *
from .serializers import *
from rest_framework import generics
from django.http import Http404


class CategoriesList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class MealsList(generics.ListAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class MealsByCategory(generics.ListAPIView):
    serializer_class = MealsSerializer
    
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if not Categories.objects.filter(id=category_id).exists():
            raise Http404()

        return Meals.objects.filter(
            category_id=category_id
        )


class MealDetail(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = MealSerializer

    def get_queryset(self):
        meal_id = self.kwargs.get('id')
        if not Meals.objects.filter(id=meal_id).exists():
            raise Http404()

        return Meals.objects.filter(
            id=meal_id
        )

