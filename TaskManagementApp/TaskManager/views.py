from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Tasks
from django.utils import timezone
def views_tasks(request):
    tasks = Tasks.objects.filter(deleted_at__isnull=True)
    template = loader.get_template('TaskManager/task_list.html')
    context = {
        'tasks': tasks,
        }
    return HttpResponse(template.render(context, request))

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        task_description = request.POST['task_description']
        task_status = request.POST['task_status']
        new_task = Tasks(task_name=task_name, task_description=task_description, task_status=task_status)
        new_task.save()
        return redirect('task_list')
    else:
        return render(request, 'TaskManager/add_task.html')

def edit_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)

    if request.method == 'POST':
        task.task_name = request.POST['task_name']
        task.task_description = request.POST['task_description']
        task.task_status = request.POST['task_status']
        task.save()  # Save the updated task object to the database
        return redirect('task_list')

    return render(request, 'TaskManager/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    task.deleted_at = timezone.now()
    task.save()
    return redirect('task_list')

