from datetime import datetime, timedelta

import pytz

from bookings.models import FitnessClass

ist = pytz.timezone("Asia/Kolkata")

FitnessClass.objects.create(
    name="Morning Yoga",
    datetime_ist=ist.localize(datetime.now() + timedelta(days=1, hours=6)),
    instructor="Shrishti",
    available_slots=10,
)

FitnessClass.objects.create(
    name="Zumba Blast",
    datetime_ist=ist.localize(datetime.now() + timedelta(days=2, hours=8)),
    instructor="Arjun",
    available_slots=15,
)

FitnessClass.objects.create(
    name="Evening Pilates",
    datetime_ist=ist.localize(datetime.now() + timedelta(days=3, hours=18)),
    instructor="Neha",
    available_slots=8,
)
