from cloudinary.forms import CloudinaryFileField
from django import forms

from recipeSharingApp.pictures.models import Gallery, Picture
from recipeSharingApp.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    picture = CloudinaryFileField(
        label='Upload Picture'
    )

    class Meta:
        model = Recipe
        exclude = ['ingredients', 'author']
        widgets = {
            'tags': forms.TextInput()
        }

    def save(self, commit=True):
        recipe = super().save(commit=False)
        picture = self.cleaned_data.get('picture')

        if commit:
            recipe.save()

            if picture:
                if hasattr(recipe, 'gallery'):
                    gallery = recipe.gallery
                else:
                    gallery = Gallery.objects.create(recipe=recipe)

                recipe_picture = Picture(image=picture, gallery=gallery)

                if len(gallery.pictures.all()) == 0:
                    recipe_picture.is_main = True

                recipe_picture.save()

        return recipe


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    pass
