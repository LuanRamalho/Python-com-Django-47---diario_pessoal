from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entrada

# Formulário de criação de usuário (registro)
class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Formulário de entrada de diário
class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['texto']
