# dolesmusic_be

## Overview

This is the backend for the Doles Music project, built with Django and Django REST Framework.

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- PostgreSQL (or another database supported by Django)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/dolesmusic_be.git
cd dolesmusic_be
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with necessary environment variables. You can use a template:

```bash
cp .env.example .env
```

Edit `.env` to set database credentials and other configuration settings.

### 5. Database Setup

Ensure your database is running and accessible. Then, run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up an admin account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/` by default.

### 8. Access the Admin Interface

Visit `http://127.0.0.1:8000/admin/` in your browser and log in with the superuser credentials.

## API Endpoints

- Leads API: `/api/leads/` (requires authentication for certain actions)

## Running with Docker

If you prefer to use Docker:

```bash
docker build -t dolesmusic_be .
docker run -p 8000:8000 dolesmusic_be
```

## Testing

Run the test suite with:

```bash
python manage.py test
```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
