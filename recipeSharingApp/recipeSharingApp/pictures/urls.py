from django.urls import path, include
from recipeSharingApp.pictures import views

urlpatterns = [
    path('<int:pk>/', include([
        path('delete/', views.DeletePictureView.as_view(), name='delete-picture'),
        path('make-main/', views.make_main_picture_view, name='make-main'),
    ]))
]