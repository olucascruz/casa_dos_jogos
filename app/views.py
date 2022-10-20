from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

from app.forms import FormCadastro, FormEntrar
# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == "GET":
        form = FormCadastro()
        context = {'form': form}
        return render(request, 'cadastro.html', context=context)
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
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.info(request, "Usuario cadastrado com sucesso!")
            return redirect('home')


def entrar(request):
    if request.method == "GET":
        form = FormEntrar()
        context = {'form': form}
        return render(request, 'entrar.html', context=context)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate( username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user:
            login_django(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, "Usuario não existe")
            return redirect('entrar')




def add_jogo(request):
    return render(request, "add_jogo.html")


