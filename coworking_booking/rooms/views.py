from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer

class RoomListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, room_id):

        try:
            room = Room.objects.get(id=room_id)
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, room_id):

        try:
            room = Room.objects.get(id=room_id)
            serializer = RoomSerializer(room, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, room_id):

        try:
            room = Room.objects.get(id=room_id)
            room.delete()
            return Response({"message": "Room deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)
