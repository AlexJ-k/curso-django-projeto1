from django.urls import path
from recipes import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('' , views.home, name= "home"), # home
    path('recipes/<int:id>/' , views.recipe, name= "recipe"), 
    path('recipes/category/<int:category_id>/' , views.category, name= "category"),
    
    
]