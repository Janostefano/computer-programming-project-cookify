from django.contrib import admin
from .models import Recipe, Ingredient, StepInstructions, StepIngredients, Comment, Tag, Category

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(StepInstructions)
admin.site.register(StepIngredients)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)

