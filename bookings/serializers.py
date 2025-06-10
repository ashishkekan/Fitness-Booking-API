import pytz
from rest_framework import serializers

from .models import Booking, FitnessClass


class FitnessClassSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()

    class Meta:
        model = FitnessClass
        fields = ["id", "name", "datetime", "instructor", "available_slots"]

    def get_datetime(self, obj):
        timezone = self.context.get("timezone", "Asia/Kolkata")
        ist_tz = pytz.timezone("Asia/Kolkata")
        target_tz = pytz.timezone(timezone)
        dt_ist = obj.datetime_ist.replace(tzinfo=ist_tz)
        dt_converted = dt_ist.astimezone(target_tz)
        return dt_converted.isoformat()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "class_id", "client_name", "client_email"]
        extra_kwargs = {"class_id": {"write_only": True}}


class BookingResponseSerializer(serializers.ModelSerializer):
    class_id = serializers.UUIDField(source="class_id.id")

    class Meta:
        model = Booking
        fields = ["id", "class_id", "client_name", "client_email"]
