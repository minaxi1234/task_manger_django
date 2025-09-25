from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TaskForm

@login_required
def home(request):
  if request.user.is_authenticated:
    tasks = Task.objects.filter(owner= request.user)
  else:
    tasks = None
  return render(request, 'home.html', {'tasks': tasks})


def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = RegisterForm()
  return render(request, 'registration/register.html', {'form':form})

def add_task(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      task = form.save(commit=False)
      task.owner = request.user
      task.save()
      return redirect('home')
  else:
    form = TaskForm()

  return render(request, 'task_form.html', {'form': form})

def update_task(request, task_id):
  task = get_object_or_404(Task, id=task_id, owner=request.user)
  if request.method == 'POST':
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = TaskForm(instance=task)
  return render(request,'task_form.html', {'form': form})

def delete_task(request, task_id):
  task = get_object_or_404(Task, id=task_id, owner=request.user)
  if request.method == 'POST':
    task.delete()
    return redirect('home')
  return render(request, 'task_confirm_delete.html', {'task':task})






