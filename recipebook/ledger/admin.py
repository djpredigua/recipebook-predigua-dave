from django.contrib import admin
from .models import RecipeIngredient, Recipe, Ingredient, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
class RecipeIngredientLine(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

# Admin for Recipe
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_on", "updated on")
    inlines = [RecipeIngredientLine]
    search_fields = ("name", "author_username")
    list_filter = ("created_on", "updated_on")

# Admin for Ingredient
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

# Profile Inline for User
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"

class CustomUserAdmin(BaseUserAdmin):
    inline = [ProfileInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(User)
admin.site.register(User, CustomUserAdmin)