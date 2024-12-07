from django.urls import path, include
from recipeSharingApp.recipes import views

urlpatterns = [
    path('create/', views.CreateRecipeView.as_view(), name='create-recipe'),
    path('trending/', views.TrendingRecipesView.as_view(), name='trending-recipes'),
    path('my-recipes/', views.MyRecipesView.as_view(), name='my-recipes'),
    path('<int:pk>/', include([
        path('', views.DetailsRecipeView.as_view(), name='recipe-details'),
        path('edit/', views.EditRecipeView.as_view(), name='edit-recipe'),
        path('delete/', views.DeleteRecipeView.as_view(), name='delete-recipe'),
    ]))
]