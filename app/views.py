from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from app.models import Game


from app.forms import FormCadastro, FormEntrar, FormAddGame
# Create your views here.

def home(request):
    games = Game.objects.all()

    context = {
        'games': games
    }
    return render(request, 'home.html', context=context)

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
            return redirect('home')
        else:
            messages.info(request, "Usuario não existe")
            return redirect('entrar')



@login_required(login_url="/entrar")
def add_jogo(request):
    if request.method == "GET":
        form = FormAddGame()
        context = {'form': form}
        return render(request, "add_jogo.html", context=context)
    else:
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        image = request.FILES.get('image')
        link = request.POST.get('link')


        game = Game.objects.filter(title=title).first()
        if game:
            messages.info(request, "Este titulo já existe")
            return redirect('add_jogo')
        else:
            user = request.user
            game = Game(title=title, subtitle=subtitle, developer=user, description=description, genre=genre, image=image, link=link)
            print(image)
            game.save()
            messages.info(request, "Game cadastrado com sucesso!")
            return redirect('home')

def sair(request):
    logout(request)
    return redirect("home")
