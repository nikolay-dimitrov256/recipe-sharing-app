from django.contrib.auth.views import LogoutView
from django.urls import path, include
from recipeSharingApp.accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
        path('delete/', views.DeleteAccountView.as_view(), name='delete-account'),
        path('delete-picture/', views.delete_profile_picture, name='delete-profile-picture')
    ]))
]