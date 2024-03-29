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


class ReservationListView(APIView):
    serializer_class = ReservationSerializer

    def get(self, request):
        reservations = Reservation.objects.all()
        if reservations:
            serializer = self.serializer_class(reservations, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            made_by = serializer.validated_data.get('made_by')
            date = serializer.validated_data.get('date')
            light_on = serializer.validated_data.get('light_on')
            facility = serializer.validated_data.get('facility')

            obj = Reservation.objects.create(made_by=made_by, date=date, facility=facility, light_on=light_on)

            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ReservationDetailView(APIView):
    serializer_class = ReservationSerializer

    def get(self, request, pk):
        reservation = Reservation.objects.filter(id=pk).first()
        if reservation:
            serializer = self.serializer_class(reservation)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        reservation = Reservation.objects.filter(id=pk).first()
        if reservation:
            reservation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)