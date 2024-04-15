from chat.chat_gpt import get_prompt_message
from chat.models import MessageGPT
from chat.models import RequestGetOptimalRouteChat
from chat.models import Vershina
from chat.serializers import ChatSerializer, GetOptimalRouteChatSerializer
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class ChatViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = MessageGPT.objects.all()
    serializer_class = ChatSerializer

    def create(self, request, *args, **kwargs):
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.save()
        return Response({"answer": answer})

    def delete(self, request, *args, **kwargs):
        MessageGPT.objects.all().delete()
        MessageGPT.objects.create(
            role="system",
            text=get_prompt_message(0)
        ).save()
        return Response("Ok")


class GetOptimalRouteChat(mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet):
    queryset = Vershina.objects.all()
    serializer_class = GetOptimalRouteChatSerializer

    def create(self, request, *args, **kwargs):
        serializer = GetOptimalRouteChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.save()
        return Response({'answer': answer})

    def delete(self, request, *args, **kwargs):
        RequestGetOptimalRouteChat.objects.all().delete()
        return Response("Ok")
