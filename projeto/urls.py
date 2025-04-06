from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # puxando as rotas (urls) do app recipes

    path('', include('recipes.urls')),
    # puxando as rotas (urls) do app recipes na rota da pagina inicial

    # puxando as rotas (urls) do app recipes na rota 'inicial/recipes/'
    # path('recipes/', include('recipes.urls')),
]

# configurando o endereço dos arquivos de media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# configurando o endereço dos arquivos estaticos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 