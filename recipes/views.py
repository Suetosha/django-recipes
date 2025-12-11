from django.views.generic import TemplateView

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

