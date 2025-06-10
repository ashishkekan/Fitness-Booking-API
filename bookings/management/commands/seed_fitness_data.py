from datetime import datetime

import pytz
from django.core.management.base import BaseCommand

from bookings.models import FitnessClass


class Command(BaseCommand):
    help = "Seeds the database with initial fitness class data"

    def handle(self, *args, **kwargs):
        ist_tz = pytz.timezone("Asia/Kolkata")
        classes = [
            {
                "name": "Yoga",
                "datetime_ist": ist_tz.localize(datetime(2025, 6, 11, 10, 0)),
                "instructor": "Shrishti",
                "available_slots": 10,
            },
            {
                "name": "Zumba",
                "datetime_ist": ist_tz.localize(datetime(2025, 6, 11, 15, 0)),
                "instructor": "Rahul",
                "available_slots": 15,
            },
            {
                "name": "HIIT",
                "datetime_ist": ist_tz.localize(datetime(2025, 6, 12, 8, 0)),
                "instructor": "Disha",
                "available_slots": 8,
            },
        ]

        for class_data in classes:
            FitnessClass.objects.create(**class_data)

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded database with fitness classes")
        )
