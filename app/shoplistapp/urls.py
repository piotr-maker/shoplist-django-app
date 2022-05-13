from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name= 'shoplist'
urlpatterns = [
    path('', views.MealsList.as_view()),
    path('<int:id>/', views.MealDetail.as_view()),
    path('categories/', views.CategoriesList.as_view()),
    path('categories/<int:category_id>', views.MealsByCategory.as_view()),
]
