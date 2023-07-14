# Authenticate

REGISTER_LOGIN
E-Commerce API - User Registration and Login

This GitHub repository contains the source code for the user registration and login functionalities of the E-Commerce API.
Features

    User registration with email, username, and password
    Password hashing for secure storage
    User login with email and password
    JWT-based authentication for API access

Technologies Used

    FastAPI: A modern, fast (high-performance), web framework for building APIs with Python
    SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping (ORM) library
    JWT: JSON Web Token for user authentication and authorization
    Passlib: Password hashing library

Getting Started

To use the registration and login functionalities of the E-Commerce API, follow the steps below:

    Clone the repository:

git clone https://github.com/your-username/e-commerce-api.git

    Navigate to the project directory:

cd e-commerce-api

markdown

    Install the dependencies:

pip install -r requirements.txt

    Configure the environment variables:

    Create a .env file in the root directory of the project.
    Add the following environment variables to the .env file:

SECRET_KEY="your-secret-key"

    Start the API server:

    uvicorn main:app --reload

    The API will be accessible at http://localhost:8000.

API Endpoints
Registration

    Endpoint: /register
    Method: POST
    Description: Register a new user.
    Request Body:
        email: User's email address (string)
        username: User's username (string)
        password: User's password (string)
    Response:
        message: Registration success message (string)

Login

    Endpoint: /login
    Method: POST
    Description: Log in an existing user.
    Request Body:
        email: User's email address (string)
        password: User's password (string)
    Response:
        access_token: JWT access token for API authentication (string)
        token_type: Token type (string)

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
License

This project is licensed under the MIT License.
