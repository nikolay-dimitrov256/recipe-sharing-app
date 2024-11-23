from django.urls import path, include
from recipeSharingApp.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
