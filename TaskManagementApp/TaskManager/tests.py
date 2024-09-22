# TaskManager/tests.py
from django.test import TestCase
from .models import Tasks
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

class TaskModelTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_task_creation(self):
        task = Tasks.objects.create(
            user=self.user,
            task_name='Test Task',
            task_description='This is a test task.',
            task_status='Pending'
        )
        self.assertEqual(task.task_name, 'Test Task')
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.task_status, 'Pending')
        self.assertIsNotNone(task.created_at)  # Ensure created_at is set


class TaskApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)

    def test_create_task_api(self):
        response = self.client.post('/api/tasks/', {
            'task_name': 'New Task',
            'task_description': 'Description for the new task.',
            'task_status': 'Pending'
        })
        self.assertEqual(response.status_code, 201)  # Check if task was created
        self.assertEqual(response.data['task_name'], 'New Task')
        self.assertEqual(response.data['task_status'], 'Pending')

    def test_list_tasks_api(self):
        # Create a task for the user
        Tasks.objects.create(
            user=self.user,
            task_name='Another Task',
            task_description='Description for another task.',
            task_status='In Progress'
        )
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)  # Check if the task list was retrieved
        self.assertEqual(len(response.data), 1)  # Ensure only one task is returned

    def test_update_task_api(self):
        # Create a task to update
        task = Tasks.objects.create(
            user=self.user,
            task_name='Task to Update',
            task_description='Old Description',
            task_status='Pending'
        )
        response = self.client.put(f'/api/tasks/{task.task_id}/', {
            'task_name': 'Updated Task',
            'task_description': 'Updated Description',
            'task_status': 'Completed'
        })
        self.assertEqual(response.status_code, 200)  # Check if task was updated
        task.refresh_from_db()
        self.assertEqual(task.task_name, 'Updated Task')

    def test_delete_task_api(self):
        # Create a task to delete
        task = Tasks.objects.create(
            user=self.user,
            task_name='Task to Delete',
            task_description='To be deleted',
            task_status='Pending'
        )
        response = self.client.delete(f'/api/tasks/{task.task_id}/')
        self.assertEqual(response.status_code, 204)  # Check if task was deleted
        self.assertEqual(Tasks.objects.count(), 0)  # Ensure no tasks are left


class UserAuthTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = '12345'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    def test_signup(self):
        response = self.client.post(reverse('auth'), {
            'signup': True,
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
            'first_name': 'New',
            'last_name': 'User'
        })
        print(response.content)  # Debugging line to inspect the response content
        self.assertEqual(response.status_code, 200)  # Check for redirect



    def test_login(self):
        response = self.client.post(reverse('auth'), {
            'login': True,
            'username': self.username,
            'password': self.password,
        })
        print(response.content)  # Debugging line
        self.assertEqual(response.status_code, 302)  # Should redirect after successful login
        self.assertRedirects(response, reverse('task_list'))  # Ensure it redirects to task list

class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Tasks.objects.create(
            user=self.user,
            task_name='Test Task',
            task_description='This is a test task.',
            task_status='Pending'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.task_name, 'Test Task')
        self.assertEqual(self.task.user, self.user)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task), 'Test Task')

class TaskApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)

    def test_create_task_api(self):
        response = self.client.post('/api/tasks/', {
            'task_name': 'New Task',
            'task_description': 'Description for the new task.',
            'task_status': 'Pending'
        })
        self.assertEqual(response.status_code, 201)  # Check if task was created
        self.assertEqual(response.data['task_name'], 'New Task')

    def test_list_tasks_api(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)  # Check if tasks are listed

    def test_retrieve_task_api(self):
        task = Tasks.objects.create(
            user=self.user,
            task_name='Another Task',
            task_description='Another task description.',
            task_status='Pending'
        )
        response = self.client.get(f'/api/tasks/{task.task_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['task_name'], 'Another Task')

    def test_update_task_api(self):
        task = Tasks.objects.create(
            user=self.user,
            task_name='Task to Update',
            task_description='Description to update.',
            task_status='Pending'
        )
        response = self.client.patch(f'/api/tasks/{task.task_id}/', {
            'task_name': 'Updated Task Name'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['task_name'], 'Updated Task Name')

    def test_delete_task_api(self):
        task = Tasks.objects.create(
            user=self.user,
            task_name='Task to Delete',
            task_description='This task will be deleted.',
            task_status='Pending'
        )
        response = self.client.delete(f'/api/tasks/{task.task_id}/')
        self.assertEqual(response.status_code, 204)  # Check if task was deleted