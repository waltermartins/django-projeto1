# from django.http import \
#     HttpResponse  # importando o protocolo http (request e response)

from django.shortcuts import \
    render  # importando a função que vai renderizar as paginas

from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):  # criando a função que vai exibir a pagina na rota inicial do site ('')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)]
    })
    # usando a função render passando os argumentos 'request' e o arquivo a ser renderizado


def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })


def usuarios(request):  # função que vai exibir a pagina da rota 'usuarios'
    return render(request, 'recipes/pages/usuarios.html', context={  # passando um dicionario no argumento context
        "nome": 'Walter Martins',  # chave e valor do dicionario
    })


def informacao(request):
    return render(request, 'recipes/pages/informacao.html')
