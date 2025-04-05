from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def exercise_list(request):
    exercises = ToDoItem.objects.filter(category=ToDoItem.EXERCISE)
    return render(request, 'exercise_list.html', {'tasks': exercises})

def stretching_list(request):
    stretching = ToDoItem.objects.filter(category=ToDoItem.STRETCHING)
    return render(request, 'stretching_list.html', {'tasks': stretching})

def cardio_list(request):
    cardio = ToDoItem.objects.filter(category=ToDoItem.CARDIO)
    return render(request, 'cardio_list.html', {'tasks': cardio})