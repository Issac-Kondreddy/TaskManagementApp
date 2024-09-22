from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='api_task_list'),  # List and create tasks
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='api_task_detail'),  # Retrieve, update, delete task
]
