from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

from . import views

app_name= 'shoplist'
urlpatterns = [
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('meals', views.MealsList.as_view()),
    path('meals/generate', views.IngredientList.as_view()),
    path('meals/<int:id>', views.MealDetail.as_view()),
    path('meals/categories', views.CategoriesList.as_view()),
    path('meals/categories/<int:category_id>', views.MealsByCategory.as_view()),
]

