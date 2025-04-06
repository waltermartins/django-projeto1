from django.test import TestCase
from django.urls import reverse  # importando o modulo reverse

# Create your tests here.


class RecipeUrlsTest(TestCase):  # a classe de testes
    def test_recipe_home_url_is_correct(self):  # testar a url de home
        # teste reverso de dentro para fora da url
        url = reverse('recipes-home')
        # se a url corresponde a pagina inicial do site
        self.assertEqual(url, '/')

    # testar a url da rota de categorias 
    def test_recipe_category_url_is_correct(self):
        # fazer o teste reverso de dentro para fora da url
        url = reverse('recipes-category', kwargs={'category_id': 1})
        self.assertEqual(url, '/category/1/')

    def test_recipes_recipe_url_is_correct(self):
        url = reverse('recipes-recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')
