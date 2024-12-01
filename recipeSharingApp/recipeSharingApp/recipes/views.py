from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from recipeSharingApp.recipes.forms import RecipeCreateForm, RecipeEditForm
from recipeSharingApp.recipes.models import Recipe


class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/create-recipe.html'

    def get_success_url(self):
        return reverse_lazy('recipe-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save()

        author = self.request.user
        self.object.author = author

        ingredients_json = self.request.POST.get('ingredients_json')

        if ingredients_json:
            self.object.ingredients = ingredients_json

        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class DetailsRecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'


class EditRecipeView(UpdateView):
    model = Recipe
    template_name = 'recipes/edit-recipe.html'
    form_class = RecipeEditForm

    def get_success_url(self):
        return reverse_lazy('recipe-details', kwargs={'pk': self.object.pk})

    def get_initial(self):
        dictionary = self.object.__dict__
        dictionary['tags'] = ' '.join(f'#{tag.name}' for tag in self.object.tags.all())

        return dictionary

    def get_object(self, queryset=None):
        recipe = Recipe.objects.select_related('author', 'gallery').prefetch_related('tags').get(pk=self.kwargs['pk'])

        return recipe

