from django.db.models import Exists, OuterRef
from django.views.generic import ListView

from recipeSharingApp.recipes.mixins import SetIsLikedInContextMixin
from recipeSharingApp.recipes.models import Recipe


class HomeView(SetIsLikedInContextMixin, ListView):
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
