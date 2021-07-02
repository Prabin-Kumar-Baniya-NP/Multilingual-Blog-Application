from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Your Password",
        widget = forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'name': 'password1',
            'id': 'password1',
            'placeholder': "Enter your Password",
                }
            )
        )
    password2 = forms.CharField(
        label="Re-type Password", 
        widget = forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'name': 'password2',
            'id': 'password2',
            'placeholder': "Enter your Password Again",
                }
            )
        )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username' : "Your Username",
            'first_name' : "Your First Name",
            'last_name': "Your Last Name",
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'username',
                'id': 'username',
                'placeholder': "Enter your Username",
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'first_name',
                'id': 'first_name',
                'placeholder': "Enter your First Name",
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'last_name',
                'id': 'last_name',
                "placeholder": "Enter your Last Name"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'name': 'email',
                'id': 'email',
                "placeholder": "Enter your Email"
            }),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Your Username",
        widget = forms.TextInput(
            attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'username',
            'placeholder': "Enter your Username",
                }
            )
        )
    password = forms.CharField(
        label="Your Password",
        widget = forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'name': 'password',
            'id': 'password',
            'placeholder': "Enter your Password",
                }
            )
        )


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username' : "Your Username",
            'first_name' : "Your First Name",
            'last_name': "Your Last Name",
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'username',
                'id': 'username',
                'placeholder': "Enter your Username",
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'first_name',
                'id': 'first_name',
                'placeholder': "Enter your First Name",
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'last_name',
                'id': 'last_name',
                "placeholder": "Enter your Last Name"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'name': 'email',
                'id': 'email',
                "placeholder": "Enter your Email"
            }),
        }

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Your Old password",
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'id' : 'old_password',
            'name': 'old_password',
            'placeholder': 'Enter your old Password',
        })
        )
    new_password1 = forms.CharField(
        label="Your New password",
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'id' : 'new_password1',
            'name': 'new_password1',
            'placeholder': 'Enter your New Password',
        })
        )
    new_password2 = forms.CharField(
        label="Re-type Password",
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'id' : 'new_password2',
            'name': 'new_password2',
            'placeholder': 'Re-type Password',
        })
        )
    