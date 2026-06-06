# fastapi_backend
# FastAPI Backend

Backend API project built with FastAPI following clean project structure and modern backend development practices.

## Features

### Authentication & Authorization

- JWT Authentication
- Access Token
- Refresh Token
- Protected Routes
- Role-Based Authorization (Admin / User)

### Database

- SQLAlchemy ORM
- SQLite Database
- Alembic Migrations

### API Features

- Full CRUD Operations
- Pagination
- Search & Filtering
- Request Validation with Pydantic

### Project Structure

- Router Layer
- Service Layer
- Schema Layer
- Core Utilities

### Logging

- Login Success Logs
- Failed Login Logs
- User Activity Logs

---

## Tech Stack

- FastAPI
- SQLAlchemy
- Alembic
- SQLite
- Pydantic
- Python-Jose (JWT)
- Passlib (Password Hashing)

---

## Project Structure

```text
fastapi_backend/
│
├── auth/
│   ├── router.py
│   ├── service.py
│   └── schema.py
│
├── user/
│   ├── model.py
│   ├── router.py
│   ├── service.py
│   └── schema.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   ├── security.py
│   ├── dependencies.py
│   └── logger.py
│
├── alembic/
│
├── main.py
├── .env
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd fastapi_backend
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows

```bash
env\Scripts\activate
```

Linux / Mac

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
DATABASE_URL=sqlite:///./test.db

SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

## Run Migrations

```bash
alembic upgrade head
```

---

## Run Server

```bash
uvicorn main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Implemented Endpoints

### Authentication

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | /auth/register | Register User |
| POST | /auth/login | Login |
| POST | /auth/refresh | Refresh Access Token |

### Users

| Method | Endpoint |
|----------|----------|
| GET | /users |
| GET | /users/me |
| GET | /users/{id} |
| POST | /users |
| PUT | /users/{id} |
| PATCH | /users/{id} |
| DELETE | /users/{id} |

---

## Learning Outcomes

This project covers:

- FastAPI Fundamentals
- API Design
- JWT Authentication
- Refresh Tokens
- SQLAlchemy ORM
- Database Migrations with Alembic
- Pagination
- Search & Filtering
- Role-Based Access Control
- Logging
- Backend Project Architecture

---

## Next Improvements

- Pytest Testing
- PostgreSQL
- Docker
- Redis
- Async SQLAlchemy
- File Uploads
- Email Verification
- Password Reset
- RAG Integration