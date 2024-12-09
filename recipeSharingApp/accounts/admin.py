from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from recipeSharingApp.accounts.forms import AppUserChangeForm, AppUserCreateForm
from recipeSharingApp.accounts.models import Profile

UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('about_me',)


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    inlines = (ProfileInline,)
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None

    list_display = ('email', 'full_name', 'date_joined',)
    search_fields = ("first_name", "last_name", "email",)
    ordering = ("email",)

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password1", "password2"),
            },
        ),
    )
    form = AppUserChangeForm
    add_form = AppUserCreateForm



