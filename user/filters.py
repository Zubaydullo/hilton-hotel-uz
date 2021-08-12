import django_filters
from django_filters import CharFilter
from .models import *


class RoomSearchForm(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = ['price', 'room_size', 'category', 'view']



class ReservationSearchForm(django_filters.FilterSet):
    class Meta:
        model = Reservation
        fields = "__all__"
        exclude = ["guest", "room","reservation_date", "email", "passport", "phone_number", "status"]