# **Django API Documentation - User CRUD** 📚

## **Overview** 🔍
This API allows managing users with CRUD operations (Create, Read, Update, Delete) to handle user data stored in the database. The user data includes a nickname (`user_nickname`), full name (`user_name`), email (`user_email`), and age (`user_age`). 👤

---

## **Models** 🏷️

### **User** 👤
The `User` model is used to represent a user in the system.

```python
class User(models.Model):
    user_nickname = models.CharField(primary_key=True, max_length=100, default="")
    user_name = models.CharField(max_length=150, default="")
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'
```

- **user_nickname**: A unique identifier for the user (Primary Key).
- **user_name**: The full name of the user.
- **user_email**: The email address of the user.
- **user_age**: The age of the user.

---

## **Views** 🖥️

### **1. `get_users`** - Get All Users
Returns a list of all users in the database.

#### **HTTP Method:** `GET` 📡

- **URL:** `/users/`
- **Success Response:** 
  - Status Code: 200 OK ✅
  - Body: List of users with `user_nickname`, `user_name`, `user_email`, `user_age`.

#### **Example Response:**

```json
[
    {
        "user_nickname": "john_doe",
        "user_name": "John Doe",
        "user_email": "john@example.com",
        "user_age": 28
    },
    {
        "user_nickname": "jane_doe",
        "user_name": "Jane Doe",
        "user_email": "jane@example.com",
        "user_age": 25
    }
]
```

---

### **2. `get_by_nick`** - Get or Update User by Nickname
Allows getting or updating a specific user by their nickname.

#### **HTTP Methods:** `GET`, `PUT`

- **URL:** `/users/<nick>/`
  - **GET**: 
    - Retrieves the details of a user based on the `user_nickname` specified.
    - **Success Response:** 200 OK ✅ with user data.
  
  - **PUT**: 
    - Updates the information of a user based on the `user_nickname` specified.
    - **Success Response:** 202 Accepted ✅ with the updated data.

#### **Example Response GET:**
```json
{
    "user_nickname": "john_doe",
    "user_name": "John Doe",
    "user_email": "john@example.com",
    "user_age": 28
}
```

---

### **3. `user_manager`** - Manage User
Allows creating, retrieving, updating, and deleting a specific user based on the nickname. Depending on the HTTP method, the operation will differ.

#### **HTTP Methods:** `GET`, `POST`, `PUT`, `DELETE`

- **URL:** `/user_manager/`
  - **GET**: 
    - Retrieves user data based on the `user_nickname` passed via query parameters.
    - **Example URL:** `/user_manager/?user=john_doe`
    - **Success Response:** 200 OK ✅ with the user data.

  - **POST**: 
    - Creates a new user with the provided data in the request body.
    - **Success Response:** 201 Created ✅ with the new user data.

  - **PUT**: 
    - Updates the user data for the specified `user_nickname`.
    - **Success Response:** 202 Accepted ✅ with the updated user data.

  - **DELETE**: 
    - Deletes the user based on the `user_nickname` provided in the request body.
    - **Success Response:** 202 Accepted ✅, indicating the user was deleted.

#### **Example Response POST:**
```json
{
    "user_nickname": "jane_doe",
    "user_name": "Jane Doe",
    "user_email": "jane@example.com",
    "user_age": 25
}
```

#### **Example Response DELETE:**
- **Status Code:** 202 Accepted ✅

---

## **Serializers** ⚙️

### **UserSerializer**
The `UserSerializer` is responsible for converting `User` model instances to JSON format to be returned by the API and validating the data received for creation or updating operations.

```python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_nickname', 'user_name', 'user_email', 'user_age']
```

---

## **URLs** 🌐

### **API URLs**

- **GET all users:** `/users/`
- **GET or PUT user by nickname:** `/users/<nick>/`
- **User management:** `/user_manager/`

---

## **Request Examples** 📬

### **GET All Users:**
```json
GET /users/
```

### **GET User by Nickname:**
```json
GET /users/john_doe/
```

### **POST Create New User:**
```json
POST /user_manager/
Content-Type: application/json
{
    "user_nickname": "new_user",
    "user_name": "New User",
    "user_email": "newuser@example.com",
    "user_age": 30
}
```

### **PUT Update User:**
```json
PUT /users/john_doe/
Content-Type: application/json
{
    "user_name": "John Doe Updated",
    "user_email": "john_updated@example.com",
    "user_age": 29
}
```

### **DELETE Delete User:**
```json
DELETE /user_manager/
Content-Type: application/json
{
    "user_nickname": "john_doe"
}
```
