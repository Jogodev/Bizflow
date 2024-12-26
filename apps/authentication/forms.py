from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=63, label="Email")
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput(), label='Mot de passe')
    password2 = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput,
        label='Confirmation Mot de passe')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=63, label="Email")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')