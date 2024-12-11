from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from recipeSharingApp.pictures.models import Picture

UserModel = get_user_model()


class DeletePictureView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Picture
    template_name = 'pictures/delete-picture.html'

    def get_success_url(self):
        if self.object.gallery.recipe:
            return reverse_lazy('recipe-details', kwargs={'pk': self.object.gallery.recipe.pk})
        elif self.object.gallery.profile:
            return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})
        return reverse_lazy('home')

    def test_func(self):
        picture = get_object_or_404(Picture, pk=self.kwargs['pk'])
        if picture.gallery.recipe:
            return picture.gallery.recipe.author == self.request.user
        elif picture.gallery.profile:
            return picture.gallery.profile.user == self.request.user
        return False


@login_required
def make_main_picture_view(request, pk):
    picture = get_object_or_404(Picture, pk=pk)

    if picture.gallery.recipe:
        if picture.gallery.recipe.author != request.user:
            return HttpResponseForbidden
    elif picture.gallery.profile:
        if picture.gallery.profile.user != request.user:
            return HttpResponseForbidden

    if request.method == 'POST':
        picture.is_main = True
        picture.save()

    return redirect(request.META.get('HTTP_REFERER'))
