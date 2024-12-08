from django.contrib import admin

from recipeSharingApp.shopping_list.models import ShoppingList


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('user__email',)
    search_fields = ('user__email',)
