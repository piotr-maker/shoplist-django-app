from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name= 'shoplist'
urlpatterns = [
    path('categories/', views.CategoriesList.as_view()),
    path('meals/', views.MealsList.as_view()),
    path('meals/<int:id>/', views.MealDetail.as_view())
]