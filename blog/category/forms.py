from django import forms

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