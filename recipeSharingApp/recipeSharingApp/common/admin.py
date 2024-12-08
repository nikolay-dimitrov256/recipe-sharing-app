from django.contrib import admin

from recipeSharingApp.common.models import Comment, Tag


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author__email', 'recipe__title', 'content',)
    list_filter = ('author__email', 'recipe__title',)
    search_fields = ('author__email', 'recipe__title', 'content',)

