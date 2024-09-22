# Task Management App

This is a Django-based Task Management application that allows users to create, edit, and manage tasks. The application has user authentication features such as login and signup, along with an API for task management.

## Features

- User Authentication (Login, Signup)
- Task Management (Create, Edit, Delete, View tasks)
- API for managing tasks (using Django REST Framework)
- Responsive UI with CSS integration

## Prerequisites

- Python 3.7 or later
- pip
- virtualenv
- AWS CLI and EB CLI for deployment on AWS Elastic Beanstalk

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/TaskManagementApp.git
    cd TaskManagementApp
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (Admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## AWS Deployment with Elastic Beanstalk

### Set up Elastic Beanstalk

1. **Initialize Elastic Beanstalk:**
    ```bash
    eb init -p python-3.7 my-django-app
    ```

2. **Create an environment and deploy:**
    ```bash
    eb create my-django-env
    eb deploy
    ```

3. **Check status of environment:**
    ```bash
    eb status
    ```

### Collect Static Files

Ensure that static files are properly collected before deployment:

```bash
python manage.py collectstatic
