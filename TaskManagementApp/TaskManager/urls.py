from django.urls import path
from . import views
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    # Web app routes
    path('', views.views_tasks, name='task_list'),  # List all tasks
    path('add/', views.add_task, name='add_task'),  # Add new task
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),  # Edit task
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Delete tas
]
