from recipeSharingApp.pictures.models import Gallery


class SetRecipeDataInContextMixin:

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        user = self.request.user

        for recipe in context['object_list']:
            recipe.is_liked = recipe.likes.filter(author=user).exists() if self.request.user.is_authenticated else False
            recipe.main_picture = recipe.gallery.pictures.filter(is_main=True).first()

        return context
