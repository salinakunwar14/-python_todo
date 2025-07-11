from django.shortcuts import render, redirect
# from django.http import HttpResponse
from todo.models import TODOAPP


def home(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            TODOAPP.objects.create(task_name=task_name, is_completed=False)
            return redirect('home')

    comp_task = TODOAPP.objects.filter(
        is_completed=False)  # 'false' changed to 'False'
    finish_task = TODOAPP.objects.filter(
        is_completed=True)  # 'true' changed to 'True'
    context = {
        'comp_task': comp_task,
        'finish_task': finish_task
    }

    return render(request, 'homes.html', context)
