from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, Profile, RecipeImage
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

# Admin for Recipe
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_on", "updated_on")
    inlines = [RecipeIngredientInline, RecipeImageInline]
    search_fields = ("name", "author_username")
    list_filter = ("created_on", "updated_on")

# Admin for Ingredient
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class RecipeImageAdmin(admin.ModelAdmin):
    list_display = ("recipe", "image", "description")

# Profile Inline for User
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"

class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)