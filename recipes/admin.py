from django.contrib import admin

# importando a classe Category, criada em models.py
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):  # criando a categoria que vai aparecer no admin do django
    ...


# registrando no admin a classe criada
admin.site.register(Category, CategoryAdmin) 


# outra forma de registrar no admin a classe criada
@admin.register(Recipe)  # usando decorator para registrar no admin a classe Recipe criada em models.py
class RecipeAdmin(admin.ModelAdmin): # criando a classe que vai aparecer no adimin do django
    ...