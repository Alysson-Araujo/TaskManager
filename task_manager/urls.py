from django.urls import path, include


from task_manager.views import user 
from task_manager.views import task 

urlpatterns = [
    path('users/', user.get_users, name='get_users'),
    path('users/<int:id>/', user.get_user_by_id, name='get_user_by_id'),
    path('users/<int:id>/tasks/', user.get_tasks_by_user_id, name='get_tasks_by_user_id'),
    path('users/<int:user_id>/tasks/<int:task_id>/', user.update_delete_user_tasks, name='update_delete_user_tasks'),
    path('users/create/', user.create_user, name='create_user'), 
    path('users/<int:id>/update/', user.update_user, name='update_user'),
    path('users/<int:id>/delete/', user.delete_user, name='delete_user'),
    path('tasks/', task.get_tasks, name='get_tasks'),
    path('accounts/', include('allauth.urls')),
]