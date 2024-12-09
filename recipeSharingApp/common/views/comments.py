from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy

from recipeSharingApp.common.forms import CommentCreateForm
from recipeSharingApp.common.models import Comment
from recipeSharingApp.recipes.models import Recipe


class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreateForm

    def get_success_url(self):
        recipe_id = self.kwargs.get('recipe_id')
        return reverse_lazy('recipe-details', kwargs={'pk': recipe_id})

    def form_valid(self, form):
        comment = form.save(commit=False)
        recipe_id = self.kwargs.get('recipe_id')
        recipe = Recipe.objects.get(pk=recipe_id)
        author = self.request.user

        comment.recipe = recipe
        comment.author = author
        comment.save()

        return HttpResponseRedirect(self.get_success_url())
