from django.contrib.messages import constants as messages
from django.shortcuts import redirect, render
from app.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(email=email).first()
        
        if user:
            messages.info(request, "Este email já existe")
            return redirect('cadastro')
        
        user = User.objects.filter(username=username).first()
        if user:
            messages.info(request, "Este username já existe")
            return redirect('cadastro')
        else:
            user = User(username, email, password)
            user.save()
            messages.info(request, "Usuario cadastrado com sucesso!")
            return redirect('')


def entrar(request):
    return render(request, 'entrar.html')

def add_jogo(request):
    return render(request, "add_jogo.html")
