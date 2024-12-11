from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestFollowUserView(TestCase):

    def setUp(self):
        self.credentials1 = {
            'email': 'user1@user.com',
            'first_name': 'Test1',
            'last_name': 'Testov',
            'password': 'asdgffegdfg'
        }
        self.credentials2 = {
            'email': 'user2@user.com',
            'first_name': 'Test2',
            'last_name': 'Testov',
            'password': 'asdgffesegeghgdfg'
        }
        self.user1 = UserModel.objects.create_user(**self.credentials1)
        self.user2 = UserModel.objects.create_user(**self.credentials2)

    def test__unfollow_user__logged_user__successfully(self):
        self.user1.following.add(self.user2)
        self.client.login(email=self.credentials1['email'], password=self.credentials1['password'])

        response = self.client.post(reverse('unfollow-user', kwargs={'pk': self.user2.pk}))
        self.user1.refresh_from_db()
        self.user2.refresh_from_db()

        self.assertNotIn(self.user2, self.user1.following.all())
        self.assertRedirects(response, reverse('profile-details', kwargs={'pk': self.user2.pk}))

    def test__follow_user__anonymous_user__expected_redirect_to_login(self):
        response = self.client.post(reverse('unfollow-user', kwargs={'pk': self.user2.pk}))

        self.assertRedirects(response, reverse('login') + '?next=/accounts/2/unfollow/')