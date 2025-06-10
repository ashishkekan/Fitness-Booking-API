import uuid

from django.db import models


class FitnessClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    datetime_ist = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.PositiveIntegerField()

    class Meta:
        db_table = "classes"

    def __str__(self):
        return f"{self.name} with {self.instructor} at {self.datetime_ist}"


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_id = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()

    class Meta:
        db_table = "bookings"

    def __str__(self):
        return f"Booking for {self.client_name} ({self.client_email})"
