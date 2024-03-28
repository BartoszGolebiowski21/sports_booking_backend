from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from sports_booking.serializers import SportsFacilitySerializer, ReservationSerializer
from sports_booking.models import SportsFacility, Reservation
from rest_framework import status


class SportsFacilityListView(APIView):
    serializer_class = SportsFacilitySerializer

    def get(self, request):
        facilities = SportsFacility.objects.all()
        serializer = self.serializer_class(facilities, many=True)
        return Response(serializer.data)


class SportsFacilityDetailView(APIView):
    serializer_class = SportsFacilitySerializer

    def get(self, request, pk):
        facility = SportsFacility.objects.filter(id=pk).first()
        if facility:
            serializer = self.serializer_class(facility)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)