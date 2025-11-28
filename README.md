# Task Management API  
Backend Assignment – ProU Technology 

Backend – API + Database

The project implements a simple **Task Management REST API** that allows managing **Employees** and **Tasks**, including linking tasks to employees and filtering tasks by status or employee.
It is built using **FastAPI + SQLite + SQLAlchemy**, following clean modular architecture.

---

## Features

- Create & List Employees  
- Create, Update, Delete & Filter Tasks  
- Link Tasks to Employees  
- Employee → Task One-to-Many Relationship  
- Input Validation using Pydantic  
- Auto-generated API Docs (Swagger)  
- Clean Modular Codebase  
- Sample JSON Data Included  


---

## Tech Stack

- **Python 3.10+**
- **FastAPI**
- **SQLite**
- **SQLAlchemy ORM**
- **Uvicorn**
- **Pydantic**

---

## Installation & Setup

### Clone the repository

```bash
git clone <your-repo-url>
cd task_management_api
```

2. Create Virtual Environment

```bash
python -m venv venv
```

3. Activate Virtual Environment

```bash
venv\Scripts\activate
```

4. Install Dependencies

```bash
pip install -r requirements.txt
```

Run the Server

```bash
uvicorn app.main:app --reload
```

### API Base URL:

```bash
http://127.0.0.1:8000
```

### Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

## JWT Authentication Guide

### 1. Login to Get Token

POST /auth/login

### Request:

```bash
{
  "username": "admin",
  "password": "admin123"
}
```

### Response:

```bash
{
  "access_token": "<token>",
  "token_type": "bearer"
}
```

### 2. Authorize in Swagger

Click Authorize → paste token.
Then protected routes will work.

## Testing

### Public Endpoints (No Login Needed)

GET /employees
GET /employees/{id}
GET /tasks
GET /tasks/{id}

### Protected Endpoints (JWT Required)

POST /tasks
PUT /tasks/{id}
DELETE /tasks/{id}

## Assumptions

- Employee email is unique.
- Tasks may exist without assignment (nullable employee_id).
- Only POST/PUT/DELETE on tasks require authentication.
- Argon2 is used for secure password hashing.
- SQLite used for simplicity and portability.

## Conclusion

This backend implements all required functionalities & bonus authentication features.
