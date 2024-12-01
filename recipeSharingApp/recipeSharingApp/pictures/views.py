from cloudinary import uploader
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from recipeSharingApp.pictures.models import Picture

UserModel = get_user_model()


@login_required
def delete_profile_picture(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    user = picture.gallery.profile.user

    if user != request.user:
        return HttpResponseForbidden('You are not allowed to edit this profile')

    if picture:
        try:
            public_id = picture.image.public_id
            uploader.destroy(public_id)
            picture.delete()
            messages.success(request, 'Profile picture deleted successfully!')

        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

    else:
        messages.error(request, message='No profile picture to delete.')

    return redirect('profile-details', user.pk)


class DeletePictureView(DeleteView):
    model = Picture
    template_name = 'pictures/delete-picture.html'

    def get_success_url(self):
        if self.object.gallery.recipe:
            return reverse_lazy('recipe-details', kwargs={'pk': self.object.gallery.recipe.pk})
        elif self.object.gallery.profile:
            return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})
        return reverse_lazy('home')
