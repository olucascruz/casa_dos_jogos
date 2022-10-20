from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('entrar/', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair'),
    path('add_jogo/', views.add_jogo, name='add_jogo'),
    path('meus_jogos/', views.meus_jogos, name='meus_jogos'),
    path('meus_jogos/edit/<int:game_pk>', views.edit_jogo, name='edit_jogo'),
    path('meus_jogos/del/<int:game_pk>', views.del_jogo, name='del_jogo'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)