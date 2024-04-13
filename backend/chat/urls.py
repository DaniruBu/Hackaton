from django.urls import path, include
from rest_framework import routers

from . import views
router = routers.DefaultRouter()
router.register(r'info', views.ChatViewSet)
router.register(r'route', views.GetOptimalRouteChat)
urlpatterns = [
    path('', include(router.urls))
]
