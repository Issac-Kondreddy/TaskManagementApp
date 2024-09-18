from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Tasks

# Create your views here.
from .models import Tasks

def views_tasks(request):
    tasks = Tasks.objects.all().values()
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