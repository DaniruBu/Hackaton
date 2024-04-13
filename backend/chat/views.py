from chat.models import MessageGPT
from chat.serializers import ChatSerializer
from rest_framework import generics
from rest_framework.response import Response


class ChatViewSet(generics.CreateAPIView):
    queryset = MessageGPT.objects.all()
    serializer_class = ChatSerializer

    def create(self, request, *args, **kwargs):
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.save()
        return Response({"answer": answer})

def roomk(request):
    return render(request, "chat/room_path.html")