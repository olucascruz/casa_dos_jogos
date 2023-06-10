from django import forms
from app.models import Game


class FormAddGame(forms.ModelForm):
    MAX_IMAGE_SIZE_MB = 1  # Tamanho máximo da imagem em megabytes

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                raise forms.ValidationError(f'A imagem não pode ter mais de {self.MAX_IMAGE_SIZE_MB} MB.')
        return image
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