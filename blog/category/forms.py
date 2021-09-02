from django import forms
from django.forms import fields, widgets
from category.models import Category
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class CategoryCreationForm(forms.Form):
    def __init__(self, requested_user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].queryset = User.objects.filter(id = requested_user_id)
        self.fields['created_by'].initial = User.objects.get(id = requested_user_id)
        self.fields['created_by'].widget = forms.HiddenInput()
        self.fields['created_by'].label = ""
    
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
        widget=CKEditorWidget()
    )
    created_by = forms.ModelChoiceField(queryset=None)

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
            'description': CKEditorWidget()
        }