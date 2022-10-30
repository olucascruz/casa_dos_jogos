from django import forms
from django.contrib.auth.models import User
from app.models import Game

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

class FormAddGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'subtitle', 'description', 'genre', 'image', 'link')
        labels = {
        "title": "Título:",
        "subtitle": "Subtítulo:",
        "description": "Descrição:",
        "genre":"Gênero:",
        "image":"Imagem:",
        "link":"Link:"
            }
        widgets ={
            'title': forms.TextInput(
                attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(
                attrs={'class':'form-control', }),
            'description': forms.Textarea(
                attrs={'class':'form-control', 'style':'resize:none;', 'rows':'5'}),
            "genre": forms.Select(
                attrs={'class':'form-control'}),
            "image": forms.FileInput(attrs={'accept':'.png, .jpg , .jpeg'}),
            'link': forms.TextInput(
                attrs={'class':'form-control',})
        }