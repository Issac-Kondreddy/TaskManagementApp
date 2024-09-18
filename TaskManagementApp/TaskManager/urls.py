from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',views.views_tasks,name= 'task_list'),
    path('tasks/add', views.add_task, name='add_task'),
]