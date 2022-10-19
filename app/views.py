from django.contrib import messages
from django.shortcuts import redirect, render
from app.models import User
from app.forms import AutoForm
from django.contrib.auth import User as UserAuth
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == "GET":
        form = AutoForm()
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
            user = User(username=username, email=email, password=password)
            user.save()
            messages.info(request, "Usuario cadastrado com sucesso!")
            return redirect('home')


def entrar(request):
    if request.method == "GET":
        return render(request, 'entrar.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)




def add_jogo(request):
    return render(request, "add_jogo.html")


