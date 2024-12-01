from django.shortcuts import render
from django.views.generic import ListView

from recipeSharingApp.recipes.models import Recipe


class HomeView(ListView):
    model = Recipe
    template_name = 'recipes/recipe-list.html'

    def get_queryset(self):
        return Recipe.objects.all().order_by('-created_at')
