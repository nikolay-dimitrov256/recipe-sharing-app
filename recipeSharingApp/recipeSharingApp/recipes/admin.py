from django.contrib import admin

from recipeSharingApp.recipes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author__email',)
    search_fields = ('title', 'description', 'instructions')
    list_filter = ('author__email',)
    ordering = ('-created_at', '-updated_at',)
    readonly_fields = ('created_at', 'updated_at')
