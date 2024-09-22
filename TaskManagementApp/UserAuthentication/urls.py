from django.urls import path
from . import views
from TaskManager.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', views.auth_view, name='auth'),  # Login and signup combined page
    path('logout/', views.logout_view, name='logout'),  # Logout
    # Task API endpoints
    path('api/tasks/', TaskListCreateView.as_view(), name='api_task_list'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='api_task_detail'),
]
