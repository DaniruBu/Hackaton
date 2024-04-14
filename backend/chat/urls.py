from django.urls import path, include
from rest_framework import routers

<<<<<<< HEAD
from . import views
router = routers.DefaultRouter()
router.register(r'info', views.ChatViewSet)
router.register(r'route', views.GetOptimalRouteChat)
urlpatterns = [
    path('', include(router.urls))
=======
from .views import *

urlpatterns = [
    path('', ChatViewSet.as_view())
>>>>>>> origin/Daryutin/frontChats
]
