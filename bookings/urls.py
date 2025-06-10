from django.urls import path

from .views import BookingCreateView, BookingListView, FitnessClassListView

urlpatterns = [
    path("classes/", FitnessClassListView.as_view(), name="class-list"),
    path("book/", BookingCreateView.as_view(), name="book-create"),
    path("bookings/", BookingListView.as_view(), name="booking-list"),
]
