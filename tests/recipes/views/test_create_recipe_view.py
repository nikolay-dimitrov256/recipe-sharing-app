from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from recipeSharingApp.recipes.models import Recipe

UserModel = get_user_model()


class TestCreateRecipeView(TestCase):

    def setUp(self):
        self.credentials = {
            'email': 'test@test.com',
            'password': 'sadgegwdefgge',
            'first_name': 'Test',
            'last_name': 'Testov',
        }

        self.user = UserModel.objects.create_user(**self.credentials)

        self.recipe_data = {
            'title': 'Test Recipe',
            'description': 'Some text',
            # 'ingredients_json': "{}",
            'instructions': 'Some longer text',
            'author': self.user.id,
        }

    def test__create_recipe_view__anonymous_user__redirects_to_login_page(self):
        response = self.client.post(reverse('create-recipe'), self.recipe_data)

        self.assertRedirects(response, reverse('login') + '?next=%2Frecipes%2Fcreate%2F')

    def test__create_recipe_view__logged_user__recipe_created_redirects_to_recipe_details(self):
        self.client.login(
            email=self.credentials['email'],
            password=self.credentials['password']
        )

        response = self.client.post(reverse('create-recipe'), self.recipe_data)
        recipe = Recipe.objects.get(title=self.recipe_data['title'])

        self.assertRedirects(response, reverse('recipe-details', kwargs={'pk': recipe.pk}))
        self.assertEqual(recipe.author.id, self.user.id)
