# Task Management App - Backend + API Integration

This project is a **Task Management App** designed to handle tasks for users. It features task creation, editing, deletion, and management along with user authentication and role management. The project is built with Django for the backend and includes comprehensive API integration.

## Features

- **User Authentication**: 
  - Sign up, login, and logout functionality.
  - User session management.
  
- **Task Management**:
  - Create, edit, and delete tasks.
  - Assign statuses to tasks.
  - View task lists filtered by status.

- **API Integration**:
  - REST APIs for task management.
  - API endpoints for user authentication and task operations.
  
- **Database**:
  - Integrated with **PostgreSQL** for secure and scalable data management.
  
## Project Structure

```bash
TaskManagementApp/
│
├── TaskManager/                  # Core Task management logic
│   ├── migrations/               # Database migration files
│   ├── static/                   # Static files like CSS, JS
│   ├── templates/                # HTML templates for views
│   ├── urls.py                   # URL routing for task management
│   ├── views.py                  # Views for task management
│   ├── models.py                 # Database models for tasks
│   ├── serializers.py            # API serializers
│   └── admin.py                  # Admin configurations
│
├── UserAuthentication/           # User authentication logic
│   ├── templates/                # HTML templates for authentication
│   ├── urls.py                   # URL routing for authentication
│   ├── views.py                  # Views for login, signup, etc.
│   ├── models.py                 # Database models for users
│   ├── serializers.py            # API serializers for user data
│   └── forms.py                  # User forms
│
├── TaskManagementApp/            # Project settings and configurations
│   ├── settings.py               # Django settings (connected to PostgreSQL)
│   ├── urls.py                   # Project-wide URL routing
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
├── requirements.txt              # Project dependencies
├── manage.py                     # Django management script
└── README.md                     # Project documentation
```
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TaskManagementApp.git
    ```
2. Navigate to the project directory:
```bash
   git clone https://github.com/yourusername/TaskManagementApp.git
```
3. Create and activate a virtual environment:
   ```bash
   python -m venv TaskAppEnv
   source TaskAppEnv/bin/activate  # On Windows: TaskAppEnv\Scripts\activate
   ```
4. Install the dependencies:
```bash
pip install -r requirements.txt
```
5. Set up the PostgreSQL database
   
   Update ```DATABASES``` in settings.py with your PostgreSQL credentials.

   Run migrations:
```bash
   python manage.py migrate
```
6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

# Authentication
1. POST ```/api/login/:``` User login.
2. POST ```/api/signup/:``` User signup.
3. POST ```/api/logout/:``` User logout.

# Task Management

1. GET ```/api/tasks/:``` Get all tasks for the authenticated user.
2. POST ```/api/tasks/:``` Create a new task.
3. PUT ```/api/tasks/<id>/:``` Update a task by ID.
4. DELETE ```/api/tasks/<id>/:``` Delete a task by ID.

# Technologies Used

Backend: Django, Django REST Framework
Database: PostgreSQL
API: Django REST API
Authentication: Django built-in authentication
Environment: Python 3.11

# Future Enhancements

Deployment on AWS or another cloud platform.
Advanced API features like token-based authentication (JWT).
Implementing a worker environment for task reminders.
Frontend integration with React or Vue.js.

## Contributing
Feel free to fork this repository and submit pull requests for any feature suggestions or bug fixes!


