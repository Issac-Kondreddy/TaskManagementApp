from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',views.views_tasks,name= 'task_list'),
    path('tasks/add', views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]