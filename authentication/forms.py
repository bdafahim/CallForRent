from django import forms
from django.contrib.auth import authenticate
from authentication.models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs=
                                                          {'placeholder': 'Password (min 6 length)', 'class':
                                                              'form-control', 'minLength': '6', 'maxLength': '12'}))


    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]