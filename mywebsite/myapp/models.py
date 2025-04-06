from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)  # Points field for the user

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ToDoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Link task to a user

    EXERCISE = 'Exercise'
    STRETCHING = 'Stretching'
    CARDIO = 'Cardio'

    CATEGORY_CHOICES = [
        (EXERCISE, 'Exercise'),
        (STRETCHING, 'Stretching'),
        (CARDIO, 'Cardio'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=11, choices=CATEGORY_CHOICES)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title