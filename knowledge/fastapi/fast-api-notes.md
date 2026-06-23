
# FastAPI Foundations Notes

## 1. Client and Server

### Client
A program that sends requests.
Examples:
- Browser
- Mobile App
- Frontend Application
- Another Backend Service

### Server
A program that receives requests, processes them, and returns responses.
Examples:
- FastAPI Application
- Django Application
- Flask Application

**Flow:**
Client → Request → Server → Response → Client

---

## 2. HTTP
HTTP is the protocol used for communication between client and server.

**Common Methods:**

### GET
Used to retrieve data.
*Example:* `GET /users/25`
*Meaning:* Get information about user 25.

### POST
Used to send data to the server.
*Example:* `POST /users`
*Meaning:* Create a new user.

### PUT
Used to update existing data.

### DELETE
Used to delete data.

---

## 3. JSON
JSON (JavaScript Object Notation) is the most common data format exchanged between client and server.

*Example:*
```json
{
  "name": "Anshu",
  "age": 28
}

````

**Important:**

  - JSON is text.
  - It is not a Python dictionary.
  - FastAPI converts JSON into Python objects internally.

-----

## 4\. Python Type Hints

*Example:*

``` python
def add(a: int, b: int) -> int:
    return a + b

```

**Purpose:**

  - Documentation
  - Editor support
  - Static analysis

*Note:* Type hints do NOT enforce types by themselves.

-----

## 5\. Pydantic

Pydantic uses type hints for:

  - Validation
  - Conversion
  - Object Creation
  - Schema Definition

*Example:*

``` python
class User(BaseModel):
    name: str
    age: int

```

**Input:**

``` json
{
  "name": "Anshu",
  "age": "28"
}

```

**Pydantic:**

1.  Validates data
2.  Converts "28" → 28
3.  Creates User object

-----

## 6\. Class and Object

### Class

Blueprint or template.
*Example:*

``` python
class Car:
    pass

```

### Object

Instance created from a class.
*Example:*

``` python
car1 = Car()

```

**Relationship:**

  - Class → Blueprint
  - Object → Actual thing created from blueprint

-----

## 7\. Attributes and Methods

### Attributes

Data stored in an object (e.g., `name`, `age`, `email`).

### Methods

Actions performed by an object (e.g., `login()`, `logout()`, `change_password()`).

**Rule:**

  - Attributes = State
  - Methods = Behavior

-----

## 8\. **init**()

Special method called automatically when an object is created.

*Example:*

``` python
class User:
    def __init__(self, name):
        self.name = name

```

**Purpose:** Initialize object data.

-----

## 9\. self

`self` refers to the current object.

*Example:*

``` python
user1 = User("Anshu")

```

  - Inside `__init__`, `self` → `user1`.
  - When another object is created (`user2 = User("Rahul")`), `self` → `user2`.

**Mental Model:** `self` = current object.

-----

## 10\. FastAPI Application Object

*Example:*

``` python
from fastapi import FastAPI
app = FastAPI()

```

**Meaning:**

  - FastAPI = Class
  - app = Object

-----

## 11\. Route

A route maps a URL to a function.

*Example:*

``` python
@app.get("/about")
def about():
    return {"page": "About"}

```

**Meaning:**
`GET /about` → `Run about()`

-----

## 12\. Route Registration

During application startup:

``` python
@app.get("/users/{user_id}")
def get_user():
    pass

```

FastAPI registers: `GET /users/{user_id}` → `get_user`. This is called Route Registration.

-----

## 13\. Decorator

*Example:*

``` python
@app.get("/users")

```

**Decorator Meaning:** Register the function below it for that route.

**Mental Model:**

  - Decorator → Attach metadata/behavior to a function
  - For FastAPI: Decorator → Register Route

-----

## 14\. Path Parameters

*Example:*

``` python
@app.get("/users/{user_id}")

```

**URL:** `/users/42`
FastAPI extracts `user_id = 42` and calls `get_user(user_id=42)`.

-----

## 15\. Request Flow

*Example:* `GET /users/42`

**Flow:**
Browser → FastAPI → Route Match → Extract `user_id = 42` → Call `get_user(42)` → Return Python dict → Convert to JSON → Response sent back

-----

## 16\. FastAPI vs Pydantic

### FastAPI Responsibilities

  - Routing
  - HTTP Requests
  - HTTP Responses
  - API Documentation
  - Request Handling

### Pydantic Responsibilities

  - Validation
  - Type Conversion
  - Object Creation
  - Schema Definition

-----

## 17\. Pydantic Object Creation

**Model:**

``` python
class User(BaseModel):
    name: str
    age: int

```

**Incoming JSON:**

``` json
{
  "name": "Anshu",
  "age": 28
}

```

**Process:**
JSON → FastAPI → Pydantic → Validate → Create User Object → Call Function

**Important:** Object creation is done automatically by Pydantic before your function runs.




## System Diagram ::

```

SERVER STARTUP
==================

Create FastAPI App
        ↓
Create User Class
        ↓
Register Routes
        ↓
Wait


CREATE USER REQUEST
=====================

Client
  ↓
POST /users
  ↓
JSON Body
  ↓
FastAPI
  ↓
Route Match
  ↓
Pydantic Validation
  ↓
Create User Object
  ↓
Call create_user()
  ↓
INSERT INTO PostgreSQL
  ↓
Return Python Dict
  ↓
Convert to JSON
  ↓
Send Response


GET USER REQUEST
============

Client
  ↓
GET /users/1
  ↓
FastAPI
  ↓
Extract id=1
  ↓
Call get_user(1)
  ↓
SELECT FROM PostgreSQL
  ↓
Return Data
  ↓
Convert to JSON
  ↓
Send Response

```