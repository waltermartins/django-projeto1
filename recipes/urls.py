from django.urls import path

from recipes import \
    views  # importando todas as funções de renderização da pasta views

# from recipes.views import (  # importando as funções que vão renderizar as páginas, em views do app recipes
#     home, informacao, usuarios)

# app_name = 'recipes'  # variavel para criação da pagina dinamica

urlpatterns = [  # rotas
    # rota inicial do site / criando um nome para a url
    path('', views.home, name='recipes-home'),
    # path('', views.home, name='home'), # com a variavel (app_name) criada podemos omitir o 'recipes'

    path('category/<int:category_id>/', views.category, name='recipes-category'),  # a rota das receitas por categoria

    # criando uma rota dinamicamente <int:id> / nome da url
    path('recipes/<int:id>/', views.recipes, name='recipes-recipe'),

    path('usuarios/', views.usuarios),  # rota usuarios
    path('informacao/', views.informacao),  # rota informações

]
