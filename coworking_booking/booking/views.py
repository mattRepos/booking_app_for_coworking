from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer

class RoomListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        rooms = Room.object.all()
        serializer = RoomSerializer(rooms, many = True)
        return Response(serializer.data)
    
class BookingListView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        