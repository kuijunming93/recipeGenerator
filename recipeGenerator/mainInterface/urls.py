from django.urls import path
from . import views

app_name = 'mainInterface'

urlpatterns = [
    path('recipe/<int:genMode>', views.recipe_view, name='generateRecipe'),
    path('generate/', views.GenerateTypeListView.as_view(), name='generateView'),
    path('repository/', views.RecipeListView.as_view(), name='recipeView'),
    path('repository/<int:pk>', views.recipe_detail, name='recipeViewDetail'),
    path('search/', views.search_view, name='searchView'),
]