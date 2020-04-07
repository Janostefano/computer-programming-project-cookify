from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory
from recipes.models import Recipe
from django.urls import reverse
from recipes.serializers import RecipesSerializer, RecipeSerializer
from rest_framework import status
import json

client = Client()


class GetRecipesTest(TestCase):
    """Test module for API GET all recipes model"""

    def setUp(self):
        Recipe.objects.create(name="Test recipe",
                              description="Test description",
                              prepareTime=100,
                              difficultyLevel="Easy",
                              numberOfPortions=2,
                              likes=5,
                              views=10,
                              category=None, photo=None)
        Recipe.objects.create(name="Test recipe 2",
                              description="Test description 2",
                              prepareTime=10,
                              difficultyLevel="Moderate",
                              numberOfPortions=4,
                              likes=10,
                              views=20,
                              category=None, photo=None)

    def test_get_all_recipes(self):
        response = client.get(reverse('recipes:recipes'))
        recipes = Recipe.objects.all()

        serializer = RecipesSerializer(recipes, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetRecipeTest(TestCase):
    """Test module to GET Recipe model with details"""

    def setUp(self):
        self.recipe = Recipe.objects.create(name="Test recipe",
                                            description="Test description",
                                            prepareTime=100,
                                            difficultyLevel="Easy",
                                            numberOfPortions=2,
                                            likes=5,
                                            views=10,
                                            category=None, photo=None)

    def test_get_valid_single_recipe(self):
        response = client.get(reverse('recipes:recipe', kwargs={'pk': self.recipe.id}))
        recipe = Recipe.objects.get(pk=self.recipe.id)

        serializer = RecipeSerializer(recipe, many=False)

        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_recipe(self):
        response = client.get(reverse('recipes:recipe', kwargs={'pk': 30}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateRecipeTest(TestCase):
    """Test module to POST method for recipes"""

    def setUp(self):
        self.valid_recipe = {
            "id": 13,
            "name": "Test Recipe",
            "description": "Very crispy chicken",
            "prepareTime": 100,
            "difficultyLevel": "low",
            "numberOfPortions": 2,
            "likes": 2,
            "views": 0,
            "category": None,
            "photo": None,
            "stepIngredients": [
            ],
            "instructions": [
            ],
            "tags": []
        }

        self.invalid_recipe = {
            'name': "Test recipe",
            'description': "Test description",
            'prepareTime': 100,
            'difficultyLevel': "Easy",
            'numberOfPortions': 2,
            'likes': 5
        }

    def test_post_valid_recipe(self):
        response = client.post(reverse('recipes:recipes'),
                               data=json.dumps(self.valid_recipe),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_recipe(self):
        response = client.post(reverse('recipes:recipes'),
                               data=json.dumps(self.invalid_recipe),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateRecipeTest(TestCase):
    """Test module to PUT recipe"""

    def setUp(self):
        self.recipeOne = Recipe.objects.create(name="Test recipe 1",
                                               description="Test description",
                                               prepareTime=100,
                                               difficultyLevel="Easy",
                                               numberOfPortions=2,
                                               likes=5,
                                               views=10,
                                               category=None, photo=None)
        self.recipeTwo = Recipe.objects.create(name="Test recipe 2",
                                               description="Test description 2",
                                               prepareTime=10,
                                               difficultyLevel="Moderate",
                                               numberOfPortions=4,
                                               likes=10,
                                               views=20,
                                               category=None, photo=None)
        self.valid_recipe = {
            "id": self.recipeOne.pk,
            "name": "Test Recipe",
            "description": "Very crispy chicken",
            "prepareTime": 100,
            "difficultyLevel": "low",
            "numberOfPortions": 2,
            "likes": 2,
            "views": 0,
            "category": None,
            "photo": None,
            "stepIngredients": [
                {
                    "name": "Breading chicken",
                    "ingredient": [
                        {
                            "name": "chicken",
                            "unit": "kg",
                            "quantity": 0,
                            "kcalPerUnit": 164,
                            "carboPerUnit": 0,
                            "proteinPerUnit": 124,
                            "fatPerUnit": 29,
                            "steps": [
                                8
                            ]
                        },
                        {
                            "name": "coating",
                            "unit": "g",
                            "quantity": 100,
                            "kcalPerUnit": 4,
                            "carboPerUnit": 4,
                            "proteinPerUnit": 0,
                            "fatPerUnit": 0,
                            "steps": [
                                8
                            ]
                        }
                    ],
                    "recipe": self.recipeOne.pk
                },
                {
                    "name": "Frying chicken",
                    "ingredient": [
                        {
                            "name": "oil",
                            "unit": "ml",
                            "quantity": 9,
                            "kcalPerUnit": 9,
                            "carboPerUnit": 0,
                            "proteinPerUnit": 0,
                            "fatPerUnit": 9,
                            "steps": [
                                9
                            ]
                        }
                    ],
                    "recipe": self.recipeOne.pk
                }
            ],
            "instructions": [
                {
                    "name": "Breading chicken",
                    "instruction": "Slice chicken and bread it in coating put on a plate. You may use your favourite seasoning",
                    "recipe": self.recipeOne.pk
                },
                {
                    "name": "Frying chicken",
                    "instruction": "Fry chicken in hot oil for about 10 minutes",
                    "recipe": self.recipeOne.pk
                }
            ],
            "tags": []
        }

    def test_valid_update_recipe(self):
        response = client.put(
            reverse('recipes:recipe', kwargs={'pk': self.recipeOne.pk}),
            data=json.dumps(self.valid_recipe),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DeleteRecipeTest(TestCase):
    def setUp(self):
        self.recipeOne = Recipe.objects.create(name="Test recipe 1",
                                               description="Test description",
                                               prepareTime=100,
                                               difficultyLevel="Easy",
                                               numberOfPortions=2,
                                               likes=5,
                                               views=10,
                                               category=None, photo=None)

    def test_delete_recipe(self):
        pk_recipe_one = self.recipeOne.pk
        response = client.delete(reverse('recipes:recipe', kwargs={'pk':pk_recipe_one}))
        response_get = client.get(reverse('recipes:recipe', kwargs={'pk':pk_recipe_one}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_non_existent_recipe(self):
        response = client.delete(reverse('recipes:recipe', kwargs={'pk': 30}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
