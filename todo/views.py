from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TODOAPP

# Create your views here.
def make_complete(request, task_id):
    task = get_object_or_404(TODOAPP, pk=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(TODOAPP, pk=task_id)
    task.delete()
    return redirect('home')


