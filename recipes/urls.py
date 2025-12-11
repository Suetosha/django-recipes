from django.urls import path
from .views import IndexView, RecipesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes/', RecipesView.as_view(), name='recipes'),
]