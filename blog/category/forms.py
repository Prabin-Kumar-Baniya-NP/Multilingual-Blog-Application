from django import forms
from django.forms import fields, widgets
from category.models import Category

class CategoryCreationForm(forms.Form):
    name = forms.CharField(
        label = "Category Name",
        max_length=24,
        widget = forms.TextInput(attrs = {
            'class': 'form-control',
            'id' : "category-name",
            'placeholder': "Enter the Category Name",
            })
        )
    description = forms.CharField(
        label= "Category Description",
        max_length=126,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': "category-description",
            'placeholder' : "Enter the Category Description",
        })
        )
    created_by = forms.CharField(
        max_length=48,
        label= "Your Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'created-by',
            'placeholder': "Enter Your Username",
        })
        )

class CategoryUpdationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            'name': forms.TextInput(attrs = {
                    'class': 'form-control',
                    'id' : "category-name",
                    'placeholder': "Enter the Category Name",
                    }),
            'description': forms.Textarea(attrs={
                    'class': 'form-control',
                    'id': "category-description",
                    'placeholder' : "Enter the Category Description",
                    })
        }