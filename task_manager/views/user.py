from django.shortcuts import render

from django.http import JsonResponse,HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from task_manager.models import User
from task_manager.serializers import serializers

import json

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        if users is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.SerializerUser(users, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_by_id(request, id):
    if request.method == 'GET':
        user = User.objects.get(pk=id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.SerializerUser(user)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tasks_by_user_id(request, id):
    if request.method == 'GET':
        user = User.objects.get(pk=id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        tasks = user.tasks.all()
        serializer = serializers.SerializerTaskUser(tasks, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = serializers.SerializerUserCreate(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, id):
    if request.method == 'PUT':
        user = User.objects.get(pk=id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = json.loads(request.body)
        serializer = serializers.SerializerUserCreate(instance=user, data=data)
        if serializer.is_valid():
            serializer.save()
            user_updated = serializers.SerializerUser(serializer.data)
            return Response(user_updated.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, id):
    if request.method == 'DELETE':
        user = User.objects.get(pk=id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# update and delete user tasks


@api_view(['PUT', 'DELETE'])
def update_delete_user_tasks(request, user_id, task_id):
    if request.method == 'PUT':
        user = User.objects.get(pk=user_id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        task = user.tasks.get(pk=task_id)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = json.loads(request.body)
        serializer = serializers.SerializerTask(instance=task, data=data)
        if serializer.is_valid():
            serializer.save()
            task_updated = serializers.SerializerTask(serializer.data)
            return Response(task_updated.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        user = User.objects.get(pk=user_id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'User not found'})
        
        task = user.tasks.get(pk=task_id)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Task not found'})
        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Task deleted'})
    
    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Bad request'})