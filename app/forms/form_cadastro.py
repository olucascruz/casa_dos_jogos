from django import forms
from django.contrib.auth.models import User

class FormCadastro(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username':"Nome de usuário",
            'password':'Senha:',
            'email':"Email:"
        }
        help_texts = {
            'username': None,
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'required':'True'})
        }