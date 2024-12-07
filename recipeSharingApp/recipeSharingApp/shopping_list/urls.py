from django.urls import path, include

from recipeSharingApp.shopping_list import views

urlpatterns = [
    path('<int:pk>/', include([
        path('', views.ShoppingListDetailView.as_view(), name='shopping-list-details'),
        path('edit/', views.edit_shopping_list_view, name='edit-shopping-list'),
        path('clear/', views.clear_shopping_list_view, name='clear-shopping-list'),
        path('<int:recipe_id>/', views.send_recipe_ingredients_to_shopping_list, name='ingredients-to-shopping-list'),
    ]))
]