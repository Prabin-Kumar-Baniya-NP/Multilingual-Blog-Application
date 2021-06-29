from django import forms
from comment.models import Comment

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["post", "body", "commented_by"]
        widgets = {
            'post': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': "post-id",
                'placeholder': "Enter the Post ID",
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'id': "comment-body",
                'placeholder': "Enter the Comment",
            }),
            'commented_by': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "username",
                'placeholder': "Enter your username",
            }),
        }