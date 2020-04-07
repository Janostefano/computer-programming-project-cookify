from rest_framework import serializers
from .models import Recipe, Ingredient, StepInstructions, StepIngredients, Comment, Tag, Category


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'unit', 'quantity', 'kcalPerUnit', 'carboPerUnit', 'proteinPerUnit', 'fatPerUnit', 'steps']


class IngredientPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'unit', 'quantity', 'kcalPerUnit', 'carboPerUnit', 'proteinPerUnit', 'fatPerUnit']


class StepIngredientsSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = StepIngredients
        fields = ['name', 'ingredient', 'recipe']


class StepIngredientsPostSerializer(serializers.ModelSerializer):
    ingredient = IngredientPostSerializer(many=True, write_only=True)

    class Meta:
        model = StepIngredients
        fields = ['name', 'ingredient']

    def create(self, validated_data):
        print("dupa")
        ingredients_data = validated_data.pop('ingredient')
        print(ingredients_data)
        instance = StepIngredients.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient = Ingredient.objects.create(**ingredient_data)
            instance.ingredients.set(ingredient)
        return instance

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredient')
        instance = super().update(instance, validated_data)
        for ingredient_data in ingredients_data:
            try:
                ingredient = Ingredient.objects.get(name=ingredients_data['name'])
                instance.ingredients.set(ingredient)
            except Ingredient.DoesNotExist:
                ingredient = Ingredient.objects.create(**ingredient_data)
                instance.ingredients.set(ingredient)
        return instance


class StepInstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepInstructions
        fields = ['name', 'instruction', 'recipe']


class StepInstructionsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepInstructions
        fields = ['name', 'instruction']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class TagPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'recipe']


class RecipeSerializer(serializers.ModelSerializer):
    stepIngredients = StepIngredientsSerializer(many=True, read_only=True)
    instructions = StepInstructionsSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'prepareTime',
                  'difficultyLevel', 'numberOfPortions', 'likes', 'views', 'category', 'photo', 'stepIngredients',
                  'instructions', 'tags']


class RecipePostSerializer(serializers.ModelSerializer):
    stepIngredients = StepIngredientsPostSerializer(many=True, write_only=True)
    instructions = StepInstructionsPostSerializer(many=True, write_only=True)
    tags = TagPostSerializer(many=True, write_only=True)

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'prepareTime',
                  'difficultyLevel', 'numberOfPortions', 'likes', 'views', 'category', 'photo', 'stepIngredients',
                  'instructions', 'tags']

    def create(self, validated_data):
        step_ingredients_data = validated_data.pop('stepIngredients')
        instructions_data = validated_data.pop('instructions')
        tags_data = validated_data.pop('tags')

        recipe = Recipe.objects.create(**validated_data)

        for step_ingredient_data in step_ingredients_data:
            ingredients_data = step_ingredient_data.pop('ingredient')
            step_ingredient = StepIngredients.objects.create(recipe=recipe, **step_ingredient_data)
            recipe.stepIngredients.add(step_ingredient)
            for ingredient_data in ingredients_data:
                ingredient = Ingredient.objects.create(**ingredient_data)
                step_ingredient.ingredient.add(ingredient)
        for instruction_data in instructions_data:
            StepInstructions.objects.create(recipe=recipe, **instruction_data)
        for tag_data in tags_data:
            Tag.objects.create(recipe=recipe, **tag_data)

        return recipe

    def update(self, instance, validated_data):
        step_ingredients_data = validated_data.pop('stepIngredients')
        instructions_data = validated_data.pop('instructions')
        tags_data = validated_data.pop('tags')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.instructions.all().delete()
        instance.stepIngredients.all().delete()
        instance.tags.all().delete()
        for instruction_data in instructions_data:
            StepInstructions.objects.create(recipe=instance, **instruction_data)
        for tag_data in tags_data:
            Tag.objects.create(recipe=instance, **tag_data)
        for step_ingredient_data in step_ingredients_data:
            ingredients_data = step_ingredient_data.pop('ingredient')
            step_ingredient = StepIngredients.objects.create(recipe=instance, **step_ingredient_data)
            for ingredient_data in ingredients_data:
                ingredient = Ingredient.objects.create(**ingredient_data)
                step_ingredient.ingredient.add(ingredient)

        return instance


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'prepareTime',
                  'difficultyLevel', 'numberOfPortions', 'likes', 'views', 'category', 'photo']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'photo']
