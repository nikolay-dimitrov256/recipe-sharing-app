from cloudinary import uploader
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView

from recipeSharingApp.pictures.models import Picture

UserModel = get_user_model()


@login_required
def delete_profile_picture(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    user = picture.profile.user

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
