from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # puxando as rotas (urls) do app recipes

    path('', include('recipes.urls')),
    # puxando as rotas (urls) do app recipes na rota da pagina inicial

    # puxando as rotas (urls) do app recipes na rota 'inicial/recipes/'
    path('recipes/', include('recipes.urls')),
]
