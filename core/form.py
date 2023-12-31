from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
# for creating form

class LoginForm(forms.Form):
    username=forms.CharField(
        # for a charfield
        widget=forms.TextInput(
            #  A widget is Django's representation of an HTML input element.
            attrs={
                "class": "form-control"
                # add bootstrap class to the form
            }
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

class SignUpForm(UserCreationForm):
    username=forms.CharField(
        # for a charfield
        widget=forms.TextInput(
            #  A widget is Django's representation of an HTML input element.
            attrs={
                "class": "form-control"
                # add bootstrap class to the form
            }
        )
    )

    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    email=forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model=User
        fields=('username','email','password1','password2','is_admin','is_customer','is_driver')