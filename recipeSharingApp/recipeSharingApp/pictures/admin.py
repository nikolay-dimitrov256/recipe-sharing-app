from django.contrib import admin

from recipeSharingApp.pictures.models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile__user__email', 'recipe',)
    search_fields = ('profile__user__email', 'recipe__title',)

