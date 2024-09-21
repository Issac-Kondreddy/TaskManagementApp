from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Tasks
from django.contrib.auth.decorators import login_required

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
        # Create a task linked to the logged-in user
        new_task = Tasks(user=request.user, task_name=task_name, task_description=task_description, task_status=task_status)
        new_task.save()
        return redirect('task_list')
    else:
        return render(request, 'TaskManager/add_task.html')

# Edit an existing task
@login_required
def edit_task(request, task_id):
    # Ensure the task belongs to the logged-in user
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
    # Ensure the task belongs to the logged-in user
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    task.deleted_at = timezone.now()  # Mark the task as deleted by setting the deleted_at time
    task.save()
    return redirect('task_list')
