from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name="home"),
    path('recipes/list/', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe_detail"),
    ]

app_name = "ledger"