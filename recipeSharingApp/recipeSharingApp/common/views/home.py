from django.db.models import Exists, OuterRef
from django.views.generic import ListView

from recipeSharingApp.recipes.models import Recipe


class HomeView(ListView):
    model = Recipe
    template_name = 'common/home.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return (Recipe.objects
                    .annotate(
                        is_followed=Exists(self.request.user.following.filter(pk=OuterRef('author_id'))))
                    .order_by('-is_followed', '-created_at', '-updated_at')
                    )
        return Recipe.objects.all().order_by('-created_at', '-updated_at')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        user = self.request.user

        for recipe in context['object_list']:
            recipe.is_liked = recipe.likes.filter(author=user).exists() if self.request.user.is_authenticated else False

        return context
