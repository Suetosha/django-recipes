from django.urls import path
from .views import IndexView, RecipesView, RecipeDetailView


app_name = 'recipes'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes/', RecipesView.as_view(), name='recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]