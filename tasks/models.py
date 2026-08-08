from django.db import models
from django.utils import timezone
from django.conf import settings

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "Новий"
        INPROGRESS = "inprogress", "В роботі"
        DONE = "done", "Виконано"

    class Priority(models.IntegerChoices):
        LOW = 1, "Низький"
        MEDIUM = 2, "Середній"
        HIGH = 3, "Високий"
        
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)
    end_date = models.DateTimeField(default=timezone.now)  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name