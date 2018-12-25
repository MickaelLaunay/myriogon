from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
