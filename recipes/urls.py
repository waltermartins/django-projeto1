from django.urls import path

from recipes.views import (  # importando as funções que vão renderizar as páginas, em views do app recipes
    home, informacao, usuarios)

urlpatterns = [  # rotas
    path('', home),  # rota inicial do site
    path('usuarios/', usuarios),  # rota usuarios
    path('informações/', informacao),  # rota informações
]
