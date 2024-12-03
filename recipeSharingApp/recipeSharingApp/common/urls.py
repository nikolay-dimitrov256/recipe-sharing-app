from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipeSharingApp.common import views
from recipeSharingApp.common.views import LikeViewSet

router = DefaultRouter()
router.register('', LikeViewSet)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('likes/', include(router.urls))
]
