from django.db import models

class CreateTodo(models.Model):
    todo = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('C', 'Completed'),
        ('P', 'Pending'),
    ]
    status = models.CharField(max_length=2, choices=status_choices)

    def __str__(self):
        return self.todo

# Create your models here.
