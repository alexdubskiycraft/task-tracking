from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    priority = models.IntegerField()
    end_date = models.DateTimeField(default=timezone.now)  
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name