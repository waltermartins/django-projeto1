from django.http import \
    HttpResponse  # importando o protocolo http (request e response)
from django.shortcuts import \
    render  # importando a função que vai renderizar as paginas


# Create your views here.
def home(request):  # criando a função que vai exibir a pagina na rota inicial do site ('')
    return render(request, 'recipes/home.html')
    # usando a função render passando os argumentos 'request' e o arquivo a ser renderizado


def usuarios(request):  # função que vai exibir a pagina da rota 'usuarios'
    return render(request, 'recipes/usuarios.html', context={  # passando um dicionario no argumento context
        "name": 'Walter Martins',  # chave e valor do dicionario
    })


def informacao(request):
    return HttpResponse('<h1>Pagina de informações</h1>')
