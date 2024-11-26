from django.urls import path
from .views import RoomListView, BookingListView

urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='room-list'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
]