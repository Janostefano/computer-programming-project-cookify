from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.recipes_list, name='recipes'),
    path('<int:pk>/', views.recipe, name='recipe'),
    path('categories/', views.categories_list, name='categories')
]
