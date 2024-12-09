from django import forms

from recipeSharingApp.common.models import Comment


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Say something'})
        }


class CommentCreateForm(CommentBaseForm):
    pass
