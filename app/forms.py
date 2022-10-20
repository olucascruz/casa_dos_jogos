from pyexpat import model
from django import forms
from django.contrib.auth.models import User


class FormCadastro(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'required':True}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'required':True})
        }
        
class FormEntrar(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'required':True})
        }