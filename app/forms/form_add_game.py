from django import forms
from app.models import Game


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