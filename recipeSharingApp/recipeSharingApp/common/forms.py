from django import forms

from recipeSharingApp.common.models import Comment


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CommentCreateForm(CommentBaseForm):
    pass
