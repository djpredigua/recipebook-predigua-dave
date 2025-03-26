from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe_detail.html"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"
    success_url = reverse_lazy("ledger:recipe_list")

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "recipe_addImage_form.html"

    def form_invalid(self, form):
        form.instance.recipe_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ledger:recipe_detail", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = Recipe.objects.get(pk=self.kwargs["pk"])
        return context 
