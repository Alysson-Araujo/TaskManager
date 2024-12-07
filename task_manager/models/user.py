from django.db import models

class User(models.Model):
    
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Email: {self.email} | Nickname: {self.nickname}'
    