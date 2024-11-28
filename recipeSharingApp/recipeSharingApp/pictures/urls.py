from django.urls import path, include
from recipeSharingApp.pictures import views

urlpatterns = [
    path('<int:pk>/', include([
        path('delete/', views.delete_profile_picture, name='delete-profile-picture')
    ]))
]