from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import *


@api_view(['GET', 'POST', 'PUT'])
def recipes_list(request):

    if request.method == 'GET':
        data = Recipe.objects.all()

        serializer = RecipesSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecipePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = RecipePostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def recipe(request, pk):
    try:
        thisRecipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(instance=thisRecipe)
        thisRecipe.category.views = thisRecipe.category.views + 1
        thisRecipe.views = thisRecipe.views + 1
        thisRecipe.save()
        thisRecipe.category.save()
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = RecipePostSerializer(thisRecipe, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PATCH":
        thisRecipe.likes += 1
        thisRecipe.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "DELETE":
        thisRecipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def categories_list(request):
    if request.method == 'GET':
        data = Category.objects.all()

        serializer = CategoriesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def category_recipes(request, pk):
    try:
        thisCategory = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = thisCategory.recipes.all()
        serializer = RecipesSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
