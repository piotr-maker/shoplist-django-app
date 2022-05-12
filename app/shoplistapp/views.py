from .models import *
from .serializers import *
from rest_framework import generics
from django.http import Http404


class MealsList(generics.ListAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class MealDetail(generics.RetrieveAPIView):
    lookup_field = 'meal_id'
    queryset = MealsIngredients.objects.all()
    serializer_class = MealSerializer

    def get_queryset(self):
        meal_id = self.kwargs.get('id')
        if not MealsIngredients.objects.filter(meal_id=meal_id).exists():
            raise Http404()

        return Meals.objects.filter(
            id=meal_id
        )

