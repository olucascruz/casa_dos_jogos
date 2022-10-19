from django import forms
from app.models import User


class AutoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'required':True}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'required':True})
        }