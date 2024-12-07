from rest_framework import serializers

from task_manager.models import Task
from task_manager.models import User

class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'nickname', 'email', 'created_at', 'updated_at']
        
        
class SerializerUserCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'nickname', 'email', 'password', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'nickname': {'required': True},
            'email': {'required': True},
            'password': {'required': True},
        }
        
        
class SerializerTask(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']



class SerializerTaskUser(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']


class UserWithTasksSerializer(serializers.ModelSerializer):
    tasks = SerializerTaskUser(many=True, read_only=True) 

    class Meta:
        model = User  
        fields = ['id', 'tasks']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'user_id': instance.id, 
            'tasks': representation['tasks']  
        }
