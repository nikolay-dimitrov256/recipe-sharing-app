from django.contrib.auth import get_user_model
from django.test import TestCase

from recipeSharingApp.recipes.forms import RecipeBaseForm

UserModel = get_user_model()


class TestRecipeBaseForm(TestCase):

    def setUp(self):
        self.form_data = {
            'title': 'Test Recipe',
            'description': 'Some text',
            'instructions': 'Some longer text',
        }

    def test__form_is_valid__true_expected(self):
        form = RecipeBaseForm(data=self.form_data)

        self.assertTrue(form.is_valid())

    def test__no_title__form_invalid_expected(self):
        self.form_data['title'] = ''

        form = RecipeBaseForm(data=self.form_data)

        self.assertFalse(form.is_valid())

    def test__no_instructions__form_invalid_expected(self):
        self.form_data['instructions'] = ''

        form = RecipeBaseForm(data=self.form_data)

        self.assertFalse(form.is_valid())

    def test__short_instructions__form_invalid_expected(self):
        self.form_data['instructions'] = 'short'

        form = RecipeBaseForm(data=self.form_data)

        self.assertFalse(form.is_valid())