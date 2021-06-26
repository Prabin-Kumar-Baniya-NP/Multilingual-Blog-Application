from django import forms
from django.forms import fields
from post.models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "category", "author"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "post-title",
                'placeholder': "Enter the Post Title",
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'id': "post-body",
                'placeholder': "Enter the Post Body",
            }),
            'category': forms.CheckboxSelectMultiple(attrs={
                'class': "form-check-input",
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "post-author",
                'placeholder': "Enter your name",
            }),
        }

class PostUpdationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "category", "author"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "post-title",
                'placeholder': "Enter the Post Title",
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'id': "post-body",
                'placeholder': "Enter the Post Body",
            }),
            'category': forms.CheckboxSelectMultiple(attrs={
                'class': "form-check-input",
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'id': "post-author",
                'placeholder': "Enter your name",
            }),
        }

