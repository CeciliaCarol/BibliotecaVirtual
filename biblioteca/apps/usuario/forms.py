from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    cpf = forms.CharField(max_length=14, required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'cpf', 'password1', 'password2']



class LoginForm(forms.Form):
    cpf = forms.CharField(max_length=14, required=True, label="CPF")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")
      