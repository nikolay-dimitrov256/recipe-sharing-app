from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from recipeSharingApp.recipes.forms import RecipeCreateForm
from recipeSharingApp.recipes.models import Recipe


class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/create-recipe.html'

    def get_success_url(self):
        return reverse_lazy('recipe-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        recipe = form.save(commit=False)
        ingredients_json = self.request.POST.get('ingredients_json')

        if ingredients_json:
            recipe.ingredients = ingredients_json

        recipe.save()

        return redirect('recipe-details', pk=recipe.pk)


class DetailsRecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'
