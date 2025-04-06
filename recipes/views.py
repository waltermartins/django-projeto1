# from django.http import \
#     HttpResponse  # importando o protocolo http (request e response)

from django.http import Http404  # importando o padrão de erro do django
from django.http import \
    HttpResponse  # importando o httpresponse para paginas não encontradas
from django.shortcuts import (  # importando a função que vai renderizar as paginas; modulo para paginas não encontradas
    get_list_or_404, get_object_or_404, render)

from utils.recipes.factory import make_recipe

from .models import Recipe  # importando a classe de dados do model.py


# Create your views here.
def home(request):  # criando a função que vai exibir a pagina na rota inicial do site ('')
    recipe = Recipe.objects.filter(
        is_publish=True  # filtrar as receitas que estão publicadas
    ).order_by('-id')  # puxando os dados do models.py
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipe
    })
    # usando a função render passando os argumentos 'request' e o arquivo a ser renderizado

def category(request, category_id):  # criando a função que vai exibir as receitas por categoria 
    # recipe = Recipe.objects.filter(
    #     category__id=category_id, is_publish=True
    # ).order_by('-id')  # puxando os dados do models.py

    # if not recipe:
    #     #return HttpResponse(render(request, 'recipes/pages/404.html'), status=404)
    #     raise Http404('Not Found')
    recipe = get_list_or_404(  # usando o modulo importado get_list para pagina não encontrada
        Recipe.objects.filter(
            category__id=category_id, is_publish=True,
        ).order_by('-id')
    )
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipe,
        #'title': f'{recipe.first().category.name} - Category |'
        'title': f'{recipe[0].category.name} - Category |'
    })
    # usando a função render passando os argumentos 'request' e o arquivo a ser renderizado


def recipes(request, id):
    # recipe = Recipe.objects.filter(
    #     pk=id,
    #     is_publish=True  # filtrar as receitas que estão publicadas
    # ).order_by('-id').first()

    recipe = get_object_or_404(Recipe, pk=id, is_publish=True) # outra forma de filtrar as receitas e retornar 404 se não encontrada

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        'title': f'{recipe.title} - {recipe.category.name}'
    })


def usuarios(request):  # função que vai exibir a pagina da rota 'usuarios'
    return render(request, 'recipes/pages/usuarios.html', context={  # passando um dicionario no argumento context
        "nome": 'Walter Martins',  # chave e valor do dicionario
    })


def informacao(request):
    return render(request, 'recipes/pages/informacao.html')
