from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import json

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        
        return Response(serializer.data)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    
    # Method GET
    if request.method == 'GET':
        try:
            if request.GET['user']:
                user_nickname = request.GET['user']
                
                try:
                    user = user.objects.get(pk=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    # Method POST
    if request.method == 'POST':
        new_user = request.data
        
        serializer = UserSerializer(data=new_user)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # Method PUT
    if request.method == 'PUT':
        nickname = request.data['user_nickname'] 
        try:
            updated_user = User.objects.get(pk=nickname)
        except:
            Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = UserSerializer(updated_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)