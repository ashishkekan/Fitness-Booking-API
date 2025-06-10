# Fitness Studio Booking API (Django)

A REST API for managing fitness class bookings built with Django, Django REST Framework, SQLite (in-memory), and Python.

## Setup Instructions

1. **Prerequisites**:
   - Python 3.8+
   - pip

2. **Installation**:
   ```bash
   pip install django djangorestframework pytz
   ```

3. **Project Setup**:
   - Create a project directory and place the provided files in the correct structure:
     ```
     fitness_studio/
     ├── fitness_studio/
     │   ├── __init__.py
     │   ├── settings.py
     │   ├── urls.py
     │   └── wsgi.py
     ├── bookings/
     │   ├── __init__.py
     │   ├── admin.py
     │   ├── apps.py
     │   ├── management/
     │   │   └── commands/
     │   │       └── seed_fitness_data.py
     │   ├── migrations/
     │   │   └── __init__.py
     │   ├── models.py
     │   ├── serializers.py
     │   ├── tests.py
     │   ├── urls.py
     │   └── views.py
     ├── manage.py
     └── README.md
     ```
   - Run migrations:
     ```bash
     python manage.py migrate
     ```
   - Seed initial data:
     ```bash
     python manage.py seed_fitness_data
     ```

4. **Running the API**:
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://localhost:8000/api/`.

5. **Running Tests**:
   ```bash
   python manage.py test
   ```

## API Endpoints

1. **GET /api/classes/**
   - Lists all upcoming classes
   - Query parameter: `timezone` (default: "Asia/Kolkata")
   - Example:
     ```bash
     curl "http://localhost:8000/api/classes/?timezone=America/New_York"
     ```

2. **POST /api/book/**
   - Books a class
   - Request body: `{ "class_id": "uuid", "client_name": "string", "client_email": "string" }`
   - Example:
     ```bash
     curl -X POST "http://localhost:8000/api/book/" \
     -H "Content-Type: application/json" \
     -d '{"class_id": "uuid-from-get-classes", "client_name": "ashish", "client_email": "ashking201299@gmail.com"}'
     ```

3. **GET /api/bookings/**
   - Lists bookings for a specific email
   - Query parameter: `client_email`
   - Example:
     ```bash
     curl "http://localhost:8000/api/bookings/?client_email=ashking201299@gmail.com"
     ```

## Features
- Timezone support using `pytz` for class datetime conversion
- Input validation using Django REST Framework serializers
- Error handling for invalid class IDs, no available slots, missing fields, and invalid timezones
- Logging for API operations
- Unit tests using Django's test framework
- Db-SQLite database with seed data
- Custom management command for seeding initial data

## Notes
- The database is initialized with sample classes in IST (Asia/Kolkata).
- All datetime fields are stored in IST and converted to the requested timezone on retrieval.
- Bookings reduce available slots and prevent overbooking.
- The API includes comprehensive error handling and logging.

## Loom Video
[A walkthrough video will be provided separately, demonstrating the API setup, endpoints, seed data command, and test execution.]
this is Loom video is in my video folder.

## Project Structure
- `bookings/`: Django project settings and main URLs
- `fitness_studio/`: Django app containing models, views, serializers, and tests
- `manage.py`: Django management script
- `README.md`: Project documentation

## Project Structure
   # Admin Credentials
- `username`: admin
- `password`: admin@123
