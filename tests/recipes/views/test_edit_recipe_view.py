from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from recipeSharingApp.recipes.models import Recipe

UserModel = get_user_model()


class TestEditRecipeView(TestCase):

    def setUp(self):
        self.credentials1 = {
            'email': 'test@test.com',
            'password': 'sadgegwdefgge',
            'first_name': 'Test',
            'last_name': 'Testov',
        }
        self.credentials2 = {
            'email': 'test2@test2.com',
            'password': 'sadgegwdsdfefgge',
            'first_name': 'Test2',
            'last_name': 'Testovski',
        }

        self.user1 = UserModel.objects.create_user(**self.credentials1)
        self.user2 = UserModel.objects.create_user(**self.credentials2)

        self.recipe_data = {
            'title': 'Test Recipe',
            'description': 'Some text',
            'instructions': 'Some longer text',
            'author': self.user1,
        }

    def test__edit_recipe_view__anonymous_user__redirects_to_login(self):
        recipe = Recipe.objects.create(**self.recipe_data)

        response = self.client.post(reverse('edit-recipe', kwargs={'pk': recipe.pk}))

        self.assertRedirects(response, reverse('login') + '?next=/recipes/1/edit/')

    def test__edit_recipe_view__own_recipe__successfully(self):
        recipe = Recipe.objects.create(**self.recipe_data)
        self.client.login(
            email=self.credentials1['email'],
            password=self.credentials1['password']
        )
        self.recipe_data['description'] = 'This is a test'
        self.recipe_data['ingredients_json'] = '{}'

        response = self.client.post(reverse('edit-recipe', kwargs={'pk': recipe.pk}), self.recipe_data)
        recipe.refresh_from_db()

        self.assertEqual(recipe.description, 'This is a test')
        self.assertRedirects(response, reverse('recipe-details', kwargs={'pk': recipe.pk}))

    def test__edit_recipe_view__other_users_recipe__expected_403_forbidden(self):
        recipe = Recipe.objects.create(**self.recipe_data)
        self.client.login(
            email=self.credentials2['email'],
            password=self.credentials2['password']
        )
        self.recipe_data['description'] = 'This is a test'
        self.recipe_data['ingredients_json'] = '{}'

        response = self.client.post(reverse('edit-recipe', kwargs={'pk': recipe.pk}), self.recipe_data)
        recipe.refresh_from_db()

        self.assertEqual(response.status_code, 403)
        self.assertEqual(recipe.description, 'Some text')
