from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # puxando as rotas (urls) do app recipes
    path('recipes/', include('recipes.urls')) # puxando as rotas (urls) do app recipes na nova rota
    
]
