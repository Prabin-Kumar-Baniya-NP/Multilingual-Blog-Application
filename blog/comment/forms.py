from django import forms
from comment.models import Comment

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["post", "body", "commented_by"]
        labels = {
            'post': '',
            'body': "Enter a new Comment",
            'commented_by': ''
        }
        widgets = {
            'post': forms.HiddenInput(attrs={
                'class': 'form-control',
                'id': "post-id",
                'placeholder': "Enter the Post ID",
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'id': "comment-body",
                'placeholder': "Enter the Comment",
            }),
            'commented_by': forms.HiddenInput(attrs={
                'class': 'form-control',
                'id': "username",
                'placeholder': "Enter your username",
            }),
        }