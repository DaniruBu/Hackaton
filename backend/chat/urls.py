from django.urls import path

from . import views

urlpatterns = [
    path('path/', views.roomk, name='path'),
    path('', views.room, name='chat'),
]
