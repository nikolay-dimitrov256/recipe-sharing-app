from django.views.generic import ListView

from recipeSharingApp.recipes.models import Recipe


class HomeView(ListView):
    model = Recipe
    template_name = 'recipes/recipe-list.html'

    def get_queryset(self):
        return Recipe.objects.prefetch_related('likes__author').all().order_by('-created_at')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        user = self.request.user

        for recipe in context['object_list']:
            recipe.is_liked = recipe.likes.filter(author=user).exists() if self.request.user.is_authenticated else False

        return context