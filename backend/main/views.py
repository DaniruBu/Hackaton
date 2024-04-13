from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Hobby, Skill, TypeImportance, TypeEvent, Events, News, Place, Schedule, Task
from .serializers import *


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbyReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = HobbySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = HobbySerializer(data=request.data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['DELETE'])
    def delete_skills(self, request, pk=None):
        serializer = HobbySerializer(instance=self.get_object())
        serializer.delete_skills(request.data.get("skills"))
        return Response(serializer.data, status=status.HTTP_200_OK)


class TypeImportanceViewSet(viewsets.ModelViewSet):
    queryset = TypeImportance.objects.all()
    serializer_class = TypeImportanceSerializer

    def update(self, request, *args, **kwargs):
        serializer = TypeImportanceSerializer(data=request.data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TypeEventViewSet(viewsets.ModelViewSet):
    queryset = TypeEvent.objects.all()
    serializer_class = TypeEventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def update(self, request, *args, **kwargs):
        serializer = PlaceSerializer(data=request.data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def update(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
