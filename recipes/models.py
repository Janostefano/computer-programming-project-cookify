from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images")
    views = models.IntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.CharField("Description", max_length=200)
    prepareTime = models.PositiveSmallIntegerField()
    difficultyLevel = models.CharField("Level of difficulty", max_length=20)
    numberOfPortions = models.PositiveSmallIntegerField()
    likes = models.IntegerField()
    views = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes", null=True, blank=True)
    photo = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.name


class StepIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="stepIngredients")
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name + " recipe: " + str(self.recipe.id)


class Ingredient(models.Model):
    units = [('g', 'gram'), ('kg', 'kilogram'),
             ('pc.', 'piece'), ('pinch', 'pinch'),
             ('tbsp', 'tablespoon'), ('ml', 'milliliters'),
             ('tsp.', "teaspoon"), ('cloves', 'cloves')]
    name = models.CharField("Name", max_length=100)
    unit = models.CharField("Units", max_length=20, choices=units)
    quantity = models.PositiveSmallIntegerField("Quantity")
    kcalPerUnit = models.SmallIntegerField("KCAL per unit")
    carboPerUnit = models.SmallIntegerField("Carbohydrates grams per unit")
    proteinPerUnit = models.SmallIntegerField("Proteins grams per unit")
    fatPerUnit = models.SmallIntegerField("Fats grams per unit")
    steps = models.ForeignKey(StepIngredients, on_delete=models.CASCADE, related_name="ingredient", null=True)

    def __str__(self):
        return self.name + " recipe: " + str(self.steps.recipe.id)


class StepInstructions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="instructions")
    name = models.CharField("Name", max_length=50)
    instruction = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + " recipe: " + str(self.recipe.id)

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    recipe = models.ManyToManyField(Recipe, related_name="tags")

    def __str__(self):
        return self.name
