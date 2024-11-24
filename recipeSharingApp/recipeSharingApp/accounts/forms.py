from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordMixin
from django import forms

UserModel = get_user_model()


class AppUserCreateForm(UserCreationForm):
    password1, password2 = SetPasswordMixin.create_password_fields()
    password1.widget.attrs['placeholder'] = 'Password'
    password2.widget.attrs['placeholder'] = 'Confirm password'
    password2.help_text = ''

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = ['email', 'first_name', 'last_name']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
