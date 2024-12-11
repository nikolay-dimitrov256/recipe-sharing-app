from django.urls import path

from recipeSharingApp.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('like/', views.LikeCreateView.as_view()),
    path('like/<int:recipe_id>/', views.LikeRetrieveDeleteView.as_view()),
    path('comment/<int:recipe_id>/', views.CreateCommentView.as_view(), name='add-comment'),
]
