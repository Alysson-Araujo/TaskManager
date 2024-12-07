from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from task_manager.models import User
from task_manager.serializers import serializers

import json

@api_view(['GET'])
def get_tasks(request):
    
    tasks = User.objects.all()
    if tasks is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    serializer = serializers.SerializerTask(tasks, many=True)
    return Response(serializer.data)
