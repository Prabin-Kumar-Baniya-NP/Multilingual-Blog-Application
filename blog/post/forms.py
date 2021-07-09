from django import forms
from django.contrib.auth.models import User
from post.models import Post

class PostCreationForm(forms.ModelForm):
    def __init__(self, requested_user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.filter(id = requested_user_id)
        self.fields['author'].initial = User.objects.get(id = requested_user_id)
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['author'].label = ""
    
    class Meta:
        model = Post
        fields = ["title", "body", "category", "author", "image"]
        labels = {
            'title': 'Post Title',
            "body": "Post Body",
            "category": "Choose Category",
            "author": "Your Username",
            "image": "Post Image"
        }
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
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': "post-image",
                'name': 'post-image'
            })
        }

class PostUpdationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "category", "image"]
        labels = {
            'title': 'Post Title',
            "body": "Post Body",
            "category": "Choose Category",
            "image": "Post Image"
        }
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
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': "post-image",
                'name': 'post-image'
            })
        }

