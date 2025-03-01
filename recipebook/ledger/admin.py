from django.contrib import admin
from .models import RecipeIngredient, Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class IngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, IngredientAdmin)