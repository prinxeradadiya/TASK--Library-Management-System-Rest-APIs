# TASK--Library-Management-System-Rest-APIs
Build a library management system that provides RESTful APIs for tracking books, borrowers, and loan transactions. The application should support operations for managing books, members, and loan records.

## Features
- Manage books: Add, update, delete, and retrieve book information.
- Manage members: Add, update, delete, and retrieve member details.
- Manage loans: Borrow and return books with fine calculation for overdue returns.

---

## Prerequisites

Before setting up the project, ensure that you have the following installed:

1. Python (version 3.8 or higher)
2. pip (Python package manager)
3. Virtualenv (recommended for environment isolation)
4. PostgreSQL or SQLite (for database management)

---

## Setup Instructions

Follow these steps to set up the application locally:


### 1. Create a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 2. Configure the Database

- The project is configured to use postgresql.

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_db',
        'USER': 'postgres',
        'PASSWORD': '3044',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Apply Migrations

Run the following commands to apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser

Create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Provide the username, email, and password as prompted.
Username : Admin
Password : 1234
### 5. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

## API Documentation

API documentation is generated using **Swagger** via `drf-yasg`. To access the Swagger UI:

1. Navigate `http://127.0.0.1:8000/swagger/`.
2. Explore available endpoints, request/response formats, and example data.

---

## Testing API Endpoints

You can test API endpoints using tools like Postman or cURL. Example endpoints:

- **Books**: `(http://127.0.0.1:8000/api/books/)`
- **Specific Book** : `(http://127.0.0.1:8000/api/books/{id})`
- **Members**: `(http://127.0.0.1:8000/api/members/)`
- **Specific Member** : `(http://127.0.0.1:8000/api/members/{id})`
- **Loans**:
  - Borrow: `(http://127.0.0.1:8000/api/loans/borrow/)`
  - Return: `(http://127.0.0.1:8000/api/loans/{id}/return_book/)`


---

## Running Tests

Run the test suite to ensure the application is functioning as expected:

```bash
python manage.py test
```

---
##For Ezquant Company - Python developer Task.
