from rest_framework import serializers

from sports_booking.models import SportsFacility, Reservation

class SportsFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsFacility
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'