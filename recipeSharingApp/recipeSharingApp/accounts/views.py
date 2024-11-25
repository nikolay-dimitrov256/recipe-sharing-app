from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from recipeSharingApp.accounts.forms import AppUserCreateForm, AppUserChangeForm, ProfileEditForm
from recipeSharingApp.accounts.mixins import AuthoriseUserMixin
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


class ProfileDetailView(LoginRequiredMixin, AuthoriseUserMixin, UserPassesTestMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'


class ProfileEditView(LoginRequiredMixin, AuthoriseUserMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/edit-profile-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class DeleteAccountView(LoginRequiredMixin, AuthoriseUserMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/delete-account-page.html'
    success_url = reverse_lazy('home')
