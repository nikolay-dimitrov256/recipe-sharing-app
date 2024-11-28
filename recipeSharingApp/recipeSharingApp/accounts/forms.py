from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordMixin
from django import forms
from cloudinary.forms import CloudinaryFileField

from recipeSharingApp.accounts.models import Profile
from recipeSharingApp.pictures.models import Picture, Gallery

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
        # fields = ['email', 'first_name', 'last_name']
        fields = '__all__'

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }


class ProfileEditForm(forms.ModelForm):
    picture = CloudinaryFileField(label='Profile Picture')

    class Meta:
        model = Profile
        exclude = ['user']

    def save(self, commit=True):
        profile = super().save(commit=False)
        picture = self.cleaned_data.get('picture')

        if commit:
            profile.save()

            if picture:
                if profile.gallery.exists():
                    gallery = profile.gallery
                else:
                    gallery = Gallery.objects.create(profile=profile)

                profile_picture = Picture(image=picture, gallery=gallery)

                gallery.refresh_from_db()

                if len(gallery) == 1:
                    profile_picture.is_main = True

                profile_picture.save()

        return profile
