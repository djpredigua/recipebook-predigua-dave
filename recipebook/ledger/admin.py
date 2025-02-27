from django.contrib import admin
from .models import RecipeIngredient, Recipe

# Register your models here.
class RecipeGroupAdmin(admin.ModelAdmin):
    model = Recipe

class RecipeAdmin(admin.ModelAdmin):
    model = RecipeIngredient

admin.site.register(Recipe, RecipeGroupAdmin)
admin.site.register(RecipeIngredient, RecipeAdmin)