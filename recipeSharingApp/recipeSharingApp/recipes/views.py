import json
from datetime import datetime, timedelta
from json import JSONDecodeError

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.db.models import F, Count
from django.db.models.functions import Now
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from recipeSharingApp.common.forms import CommentCreateForm
from recipeSharingApp.recipes.forms import RecipeCreateForm, RecipeEditForm
from recipeSharingApp.recipes.mixins import SetRecipeDataInContextMixin
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

        try:
            ingredients = json.loads(ingredients_json)
        except JSONDecodeError:
            return self.form_invalid(form)

        self.object.ingredients = ingredients
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class DetailsRecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentCreateForm()

        user = self.request.user
        recipe = context['object']
        recipe.is_liked = recipe.likes.filter(author=user).exists() if self.request.user.is_authenticated else False

        return context


class EditRecipeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])

        return recipe.author == self.request.user

    def form_valid(self, form):
        ingredients_json = self.request.POST.get('ingredients_json')

        try:
            ingredients = json.loads(ingredients_json)
        except JSONDecodeError:
            return self.form_invalid(form)

        self.object.ingredients = ingredients
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class DeleteRecipeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/delete-recipe.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])

        return recipe.author == self.request.user


class TrendingRecipesView(SetRecipeDataInContextMixin, ListView):
    model = Recipe
    template_name = 'recipes/trending-recipes.html'

    def get_queryset(self):
        return (
            Recipe.objects
            .annotate(likes_count=Count('likes'))
            .filter(created_at__gte=Now() - timedelta(days=7))
            .order_by('-likes_count')
        )


class MyRecipesView(LoginRequiredMixin, SetRecipeDataInContextMixin, ListView):
    model = Recipe
    template_name = 'recipes/my-recipes.html'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user).order_by('-created_at', '-updated_at')
