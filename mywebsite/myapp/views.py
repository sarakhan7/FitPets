from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import ToDoItem
from django.shortcuts import get_object_or_404



# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')  # Make sure to create this template

def login(request):
    return render(request, 'myapp/login.html')

def register(request):
    return render(request, 'myapp/register.html')

def task_list(request):
    tasks = ToDoItem.objects.all()  # Get all tasks from the database
    return render(request, 'your_template.html', {'tasks': tasks})

def exercise_list(request):
    exercises = ToDoItem.objects.filter(category=ToDoItem.EXERCISE, completed=False)  # Exclude completed tasks
    return render(request, 'exercise_list.html', {'tasks': exercises})

def add_exercise_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Get the task title from the form
        if title:
            ToDoItem.objects.create(title=title, category=ToDoItem.EXERCISE)  # Create a new task
        return redirect('exercise_list')  # Redirect back to the exercise list


def mark_task_complete(request, task_id):
    task = get_object_or_404(ToDoItem, id=task_id)
    task.completed = True
    task.save()
    return redirect('exercise_list')  # Redirect back to the exercise list

def stretching_list(request):
    stretching = ToDoItem.objects.filter(category=ToDoItem.STRETCHING)
    return render(request, 'stretching_list.html', {'tasks': stretching})

def cardio_list(request):
    cardio = ToDoItem.objects.filter(category=ToDoItem.CARDIO)
    return render(request, 'cardio_list.html', {'tasks': cardio})