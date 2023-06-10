from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from app.models import Game


from app.forms.form_cadastro import FormCadastro
from app.forms.form_entrar import FormEntrar
from app.forms.form_add_game import FormAddGame

# Create your views here.

def home(request):
    games = Game.objects.all()

    context = {
        'games': games,
        'alt': f"Imagem do jogo {games.name}"
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
        if user:
            login_django(request, user)
            return redirect('home')
        else:
            return redirect('entrar')


@login_required(login_url="/entrar")
def add_jogo(request):
    if request.method == "GET":
        form = FormAddGame()
        context = {'form': form}
        return render(request, "add_jogo.html", context=context)
    else:
        form = FormAddGame(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            subtitle = form.cleaned_data['subtitle']
            description = form.cleaned_data['description']
            genre = form.cleaned_data['genre']
            image = form.cleaned_data['image']
            link = form.cleaned_data['link']
        
            

            game = Game.objects.filter(title=title).first()
            if game:
                messages.info(request, "Este titulo já existe")
            elif image == None:
                messages.info(request, "Coloque uma imagem")
            else:
                user = request.user
                game = Game(title=title, subtitle=subtitle, developer=user, description=description, genre=genre, image=image, link=link)
                
                game.save()
                return redirect('home')
        else:
            # O formulário é inválido, tratar os erros
            messages.error(request, "Formulário inválido")
            context = {'form': form}
            return render(request, "add_jogo.html", context=context)

@login_required(login_url="/entrar")
def sair(request):
    logout(request)
    return redirect("home")


@login_required(login_url="/entrar")
def meus_jogos(request):
    games = Game.objects.filter(developer = request.user)

    context = {
        'games': games
    }
    return render(request, "meus_jogos.html", context=context)


def edit_jogo(request, game_pk):
    game =  Game.objects.get(pk=game_pk)

    form = FormAddGame(request.POST or None, instance=game)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('meus_jogos')

    context = {
        'game': game.id,
        'form': form,
    }
    return render(request, 'edit_jogo.html', context)


def del_jogo(request, game_pk):
    game = Game.objects.get(pk=game_pk)
    game.delete()
    return redirect('meus_jogos')