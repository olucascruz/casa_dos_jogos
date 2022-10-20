from django import forms
from django.contrib.auth.models import User
from app.models import Game

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

class FormAddGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'subtitle', 'description', 'genre', 'image')
        labels = {
        "title": "Título:",
        "subtitle": "Subtítulo:",
        "description": "Descrição:",
        "genre":"Gênero:",
        "image":"Imagem:"
            }
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control', }),
            'description': forms.Textarea(attrs={'class':'form-control', 'style':'resize:none;', 'rows':'8'}),
        }