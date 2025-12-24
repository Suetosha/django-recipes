from django.views.generic import TemplateView, DetailView

from recipes.mixins import TitleMixin
from recipes.models import Recipe


class IndexView(TitleMixin, TemplateView):
    template_name = "index.html"
    title = "Главная страница"


class RecipesView(TitleMixin, TemplateView):
    template_name = "receipts.html"
    title = "Рецепты"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_type = self.request.GET.get('type')

        if filter_type:
            context['recipes'] = Recipe.objects.filter(type=filter_type)
        else:
            context['recipes'] = Recipe.objects.all()

        return context


class RecipeDetailView(TitleMixin, DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"

    def get_title(self):
        return self.object.name