import logging

import pytz
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking, FitnessClass
from .serializers import (
    BookingResponseSerializer,
    BookingSerializer,
    FitnessClassSerializer,
)

logger = logging.getLogger(__name__)


class FitnessClassListView(APIView):
    def get(self, request):
        timezone_param = request.query_params.get("timezone", "Asia/Kolkata")
        try:
            pytz.timezone(timezone_param)
        except pytz.exceptions.UnknownTimeZoneError:
            logger.warning(f"Invalid timezone: {timezone_param}")
            return Response(
                {"error": "Invalid timezone"}, status=status.HTTP_400_BAD_REQUEST
            )

        classes = FitnessClass.objects.filter(datetime_ist__gt=timezone.now())
        serializer = FitnessClassSerializer(
            classes, many=True, context={"timezone": timezone_param}
        )
        logger.info(f"Retrieved {len(classes)} classes for timezone {timezone_param}")
        return Response(serializer.data)


class BookingCreateView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning(f"Invalid booking data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            fitness_class = FitnessClass.objects.get(
                id=serializer.validated_data["class_id"].id
            )
            if fitness_class.available_slots <= 0:
                logger.warning(f"No slots available for class_id: {fitness_class.id}")
                return Response(
                    {"error": "No slots available"}, status=status.HTTP_400_BAD_REQUEST
                )

            booking = serializer.save()
            fitness_class.available_slots -= 1
            fitness_class.save()

            response_serializer = BookingResponseSerializer(booking)
            logger.info(f"Booking created: {booking.id} for {booking.client_email}")
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        except FitnessClass.DoesNotExist:
            logger.warning(
                f"Invalid class_id: {serializer.validated_data['class_id'].id}"
            )
            return Response(
                {"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f"Error creating booking: {str(e)}")
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class BookingListView(APIView):
    def get(self, request):
        client_email = request.query_params.get("client_email")
        if not client_email:
            logger.warning("Missing client_email parameter")
            return Response(
                {"error": "client_email is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        bookings = Booking.objects.filter(client_email=client_email)
        serializer = BookingResponseSerializer(bookings, many=True)
        logger.info(f"Retrieved {len(bookings)} bookings for {client_email}")
        return Response(serializer.data)
