"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import home
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tasks/', views.task_list, name='task_list'),
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('stretching/', views.stretching_list, name='stretching_list'),
    path('cardio/', views.cardio_list, name='cardio_list'),
    path('exercises/add/', views.add_exercise_task, name='add_exercise_task'),
    path('exercises/complete/<int:task_id>/', views.mark_task_complete, name='mark_task_complete') # Add this line
]
