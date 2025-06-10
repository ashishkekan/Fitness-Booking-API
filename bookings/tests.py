import uuid
from datetime import datetime

import pytz
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Booking, FitnessClass


class FitnessStudioTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        ist_tz = pytz.timezone("Asia/Kolkata")
        self.class1 = FitnessClass.objects.create(
            id=uuid.uuid4(),
            name="Yoga",
            datetime_ist=ist_tz.localize(datetime(2025, 6, 11, 10, 0)),
            instructor="Shrishti",
            available_slots=10,
        )

    def test_get_classes(self):
        response = self.client.get("/api/classes/?timezone=Asia/Kolkata")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["name"], "Yoga")

    def test_book_class(self):
        booking_data = {
            "class_id": str(self.class1.id),
            "client_name": "ashish",
            "client_email": "ashking201299@gmail.com",
        }
        response = self.client.post("/api/book/", booking_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["client_email"], "ashking201299@gmail.com")
        self.class1.refresh_from_db()
        self.assertEqual(self.class1.available_slots, 9)

    def test_book_class_no_slots(self):
        self.class1.available_slots = 0
        self.class1.save()
        booking_data = {
            "class_id": str(self.class1.id),
            "client_name": "ashish",
            "client_email": "ashking201299@gmail.com",
        }
        response = self.client.post("/api/book/", booking_data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("No slots available", response.json()["error"])

    def test_get_bookings(self):
        booking = Booking.objects.create(
            class_id=self.class1,
            client_name="ashish",
            client_email="ashking201299@gmail.com",
        )
        response = self.client.get(
            "/api/bookings/?client_email=ashking201299@gmail.com"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["client_email"], "ashking201299@gmail.com")
