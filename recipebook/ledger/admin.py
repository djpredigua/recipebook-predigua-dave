from django.contrib import admin
from .models import RecipeIngredient, Recipe, Ingredient

# Register your models here.
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RecipeIngredientInline] 

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity') 


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)