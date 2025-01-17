from django.db.models import Exists, OuterRef, Q, F
from django.views.generic import ListView

from recipeSharingApp.recipes.mixins import SetRecipeDataInContextMixin
from recipeSharingApp.recipes.models import Recipe


class HomeView(SetRecipeDataInContextMixin, ListView):
    model = Recipe
    template_name = 'common/home.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return (Recipe.objects
                    .annotate(
                        is_followed=Exists(self.request.user.following.filter(pk=OuterRef('author_id')))
                        |
                        Q(author=self.request.user)
                    )
                    .order_by('-is_followed', '-created_at', '-updated_at')
                    )
        return Recipe.objects.all().order_by('-created_at', '-updated_at')
