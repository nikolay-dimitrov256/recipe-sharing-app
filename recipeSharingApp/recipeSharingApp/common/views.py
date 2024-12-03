from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from recipeSharingApp.common.models import Like
from recipeSharingApp.common.serializers import LikeSerializer
from recipeSharingApp.recipes.models import Recipe


class HomeView(ListView):
    model = Recipe
    template_name = 'recipes/recipe-list.html'

    def get_queryset(self):
        return Recipe.objects.all().order_by('-created_at')


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.all()
