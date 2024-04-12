from django.urls import path
from django.urls.conf import include
from main import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hobby', views.HobbyViewSet)
router.register(r'skill', views.SkillViewSet)
router.register(r'type-importance', views.TypeImportanceViewSet)
router.register(r'type-event', views.TypeEventViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'place', views.PlaceViewSet)
router.register(r'schedule', views.ScheduleViewSet)
urlpatterns = [
    path('', include(router.urls)),
]