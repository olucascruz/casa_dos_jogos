from django import forms
from django.contrib.auth.models import User


class FormEntrar(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
            'username': None,
        }
        labels = {
            'username':"Nome de usuário",
            'password':'Senha:'
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }