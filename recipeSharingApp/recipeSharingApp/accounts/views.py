from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from cloudinary import uploader

from recipeSharingApp.accounts.forms import AppUserCreateForm, ProfileEditForm
from recipeSharingApp.accounts.models import Profile

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/edit-profile-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])

        return self.request.user == profile.user


class DeleteAccountView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/delete-account-page.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])

        return self.request.user == profile.user


def follow_user(request, pk):
    follower = request.user
    followed = UserModel.objects.get(pk=pk)

    follower.following.add(followed)

    return redirect('profile-details', pk=pk)


def unfollow_user(request, pk):
    follower = request.user
    followed = UserModel.objects.get(pk=pk)

    follower.following.remove(followed)

    return redirect('profile-details', pk=pk)
