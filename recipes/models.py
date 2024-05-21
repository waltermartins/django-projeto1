from django.contrib.auth.models import \
    User  # importando o model usuario do django
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)


class Recipe(models.Model):
    # criando as colunas do banco de dados
    title = models.CharField(max_length=65)  # maximo de 65 caracteres
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()  # campo só recebe inteiros
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    # campo que recebe um valor boleano. False por padrão
    preparation_steps_is_html = models.BooleanField(default=False)
    # campo que recebe uma data. autocriação como True
    created_at = models.DateTimeField(auto_now_add=True)
    # recebe uma data. auto atualiza se editado
    update_at = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)
    # ao trabalhar com imagens, instalar o pillow. pip install pillow
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')

    category = models.ForeignKey(  # fazendo relação com a classe Categoria
        # se a categoria for apagada, campo será 'null'
        Category, on_delete=models.SET_NULL, null=True)

    author = models.ForeignKey(  # fazendo relação com a classe User, importada do django
        # se a categoria for apagada, campo será 'null'
        User, on_delete=models.SET_NULL, null=True)
