from django.db import models

class Task(models.Model):
    
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return f'Title: {self.title} | Status: {self.status}'
    