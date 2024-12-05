from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipeSharingApp.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('like/', views.LikeCreateView.as_view()),
    path('unlike/<int:recipe_id>/', views.LikeDeleteView.as_view()),
    path('get-likes/<int:recipe_id>/', views.LikesRetrieveView.as_view())
]
