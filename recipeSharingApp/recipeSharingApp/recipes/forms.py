from cloudinary.forms import CloudinaryFileField
from django import forms

from recipeSharingApp.common.models import Tag
from recipeSharingApp.pictures.models import Gallery, Picture
from recipeSharingApp.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    picture = CloudinaryFileField(
        label='Upload Picture',
        required=False,
    )

    tags = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': '#tag1 #tag2 #tag3...'})
    )

    class Meta:
        model = Recipe
        exclude = ['ingredients', 'author', 'tags']

    def save(self, commit=True):
        recipe = super().save(commit=False)
        picture = self.cleaned_data.get('picture')
        tags = self.cleaned_data.get('tags', '')

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

            input_tags_names = [name.strip() for name in tags.split('#')]
            existing_tags = Tag.objects.filter(name__in=input_tags_names)
            tags_to_create = list(set(input_tags_names) - set(existing_tags.values_list('name', flat=True)))

            tags_to_create = [
                    Tag(name=tag.strip())
                    for tag in tags_to_create
                    if 0 < len(tag.strip()) <= Tag.TAG_MAX_LENGTH
                ]

            created_tags = Tag.objects.bulk_create(tags_to_create)

            recipe_tags = created_tags + list(existing_tags)
            recipe.tags.set(recipe_tags)

        return recipe


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    pass
