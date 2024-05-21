from django.urls import path

from recipes import \
    views  # importando todas as funções de renderização da pasta views

# from recipes.views import (  # importando as funções que vão renderizar as páginas, em views do app recipes
#     home, informacao, usuarios)


urlpatterns = [  # rotas
    path('', views.home),  # rota inicial do site
    path('usuarios/', views.usuarios),  # rota usuarios
    path('informacao/', views.informacao),  # rota informações
    # criando uma rota dinamicamente <int:id>
    path('recipes/<int:id>/', views.recipes),
]
