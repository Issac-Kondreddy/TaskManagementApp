from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Tasks
from django.core.exceptions import ValidationError  # Add this import

from rest_framework import generics
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

# View tasks for the logged-in user
@login_required
def views_tasks(request):
    tasks = Tasks.objects.filter(user=request.user, deleted_at__isnull=True)
    template = loader.get_template('TaskManager/task_list.html')
    context = {
        'tasks': tasks,
        'first_name': request.user.first_name  # Pass the first name to the template
    }
    return HttpResponse(template.render(context, request))


# Add a new task for the logged-in user
@login_required
def add_task(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        task_description = request.POST['task_description']
        task_status = request.POST['task_status']

        errors = {}

        # Validation logic
        if len(task_name) < 5:
            errors['task_name'] = ['Task name should be at least 5 characters long.']
        
        if errors:
            # Return form with errors and previously entered data
            return render(request, 'TaskManager/add_task.html', {
                'errors': errors,
                'task_name': task_name,
                'task_description': task_description,
                'task_status': task_status,
            })

        # Create a task linked to the logged-in user
        new_task = Tasks(user=request.user, task_name=task_name, task_description=task_description, task_status=task_status)
        new_task.save()
        return redirect('task_list')
    else:
        return render(request, 'TaskManager/add_task.html')
# Edit an existing task
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)

    if request.method == 'POST':
        task.task_name = request.POST['task_name']
        task.task_description = request.POST['task_description']
        task.task_status = request.POST['task_status']
        task.save()  # Save the updated task object to the database
        return redirect('task_list')

    return render(request, 'TaskManager/edit_task.html', {'task': task})

# Soft delete a task by setting the deleted_at timestamp
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    task.deleted_at = timezone.now()  # Mark the task as deleted by setting the deleted_at time
    task.save()
    return redirect('task_list')

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get query parameter for task_status
        status = self.request.query_params.get('status', None)
        queryset = Tasks.objects.filter(user=self.request.user, deleted_at__isnull=True)
        if status:
            queryset = queryset.filter(task_status=status)
        return queryset


# Retrieve, update, or delete a specific task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    # Filter tasks to show only those of the logged-in user
    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
