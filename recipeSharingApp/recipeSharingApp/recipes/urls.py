from django.urls import path, include
from recipeSharingApp.recipes import views

urlpatterns = [
    path('create/', views.CreateRecipeView.as_view(), name='create-recipe'),
    path('<int:pk>/', include([
        path('', views.DetailsRecipeView.as_view(), name='recipe-details'),
        path('edit/', views.EditRecipeView.as_view(), name='edit-recipe'),
    ]))
]