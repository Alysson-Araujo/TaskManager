from django.contrib import admin

from task_manager.models.task import Task
from task_manager.models.user import User

admin.site.register(User)
admin.site.register(Task)
