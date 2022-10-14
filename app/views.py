from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'cadastro.html')
    
def entrar(request):
    return render(request, 'entrar.html')