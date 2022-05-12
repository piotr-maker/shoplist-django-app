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


class MealDetail(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = MealsIngredients.objects.all()
    serializer_class = MealSerializer

    def get_queryset(self):
        meal_id = self.kwargs.get('id')
        if not Meals.objects.filter(id=meal_id).exists():
            raise Http404()

        return Meals.objects.filter(
            id=meal_id
        )

