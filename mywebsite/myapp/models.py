from django.db import models

# Create your models here.
class ToDoItem(models.Model):
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