## User Management API
![Capture](https://github.com/Muhammadhidayatullahaspar/FastAPI_UserManagement/assets/100209360/0ce4c388-3a1b-4e2a-8e7c-2467c39a15ed)

# Description
User Management API is a back-end system designed for managing users within an application or platform. This API facilitates basic operations such as user registration, authentication, and CRUD (Create, Read, Update, Delete) functionalities for user management.
This project is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. Speed and ease of use are the main advantages of this framework.

![Capture2](https://github.com/Muhammadhidayatullahaspar/FastAPI_UserManagement/assets/100209360/6e3c589b-42ac-4e11-8c46-3e6073a2ccf3)

# Features
1. User Authentication: Register and log in using JWT (JSON Web Tokens) for security and efficient session management.
2. CRUD Operations: Functionalities to create, read, update, and delete users.
3. Token Management: Ensures secure and efficient user sessions.
4. Swagger UI: Interactive documentation created by FastAPI to test and demonstrate the API.

# Technologies
1. FastAPI: For fast and efficient API construction.
2. SQLAlchemy: As an ORM (Object Relational Mapper) for database interactions.
3. Pydantic: For data validation and environment settings.
4. SQLite: As the backend database for data storage.
5. Python 3.7+: As the primary programming language.

# How to Run
1. Clone this repository.
2. Install the required dependencies:
   pip install -r requirements.txt
3. Run the local server:
   uvicorn main:app --reload
   The API will be available at http://127.0.0.1:8000.
4. Access the Swagger UI at http://127.0.0.1:8000/docs to view the documentation and interact with the API.

# Contributing
Contributions to this project are highly appreciated. If you would like to contribute, please fork this repository, make your changes, and submit a pull request.
