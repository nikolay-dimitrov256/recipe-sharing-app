from django.shortcuts import get_object_or_404

from recipeSharingApp.accounts.models import Profile


class AuthoriseUserMixin:  # Not used. To be deleted
    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])

        return self.request.user == profile.user